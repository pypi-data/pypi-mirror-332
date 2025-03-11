"""Data utilities."""

import abc
import math
from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import numpy.typing as npt
import polars as pl
import polars.selectors as cs
import torch
from polars.interchange.protocol import SupportsInterchange
from torch.nn.utils.rnn import pad_sequence
from tqdm import tqdm

from fastabx.utils import Environment
from fastabx.verify import verify_empty_datapoints

type FeatureMaker = Callable[[str | Path], torch.Tensor]
type ArrayLike = npt.ArrayLike


@dataclass(frozen=True)
class Batch:
    """Batch of padded data."""

    data: torch.Tensor
    sizes: torch.Tensor

    def __repr__(self) -> str:
        return f"Batch(data=Tensor(shape={self.data.shape}, dtype={self.data.dtype}), sizes={self.sizes})"


class DataAccessor(abc.ABC):
    """Abstract class for data accessors.

    A data accessor is a way to access a torch.Tensor given an index.
    """

    @abc.abstractmethod
    def __getitem__(self, i: int) -> torch.Tensor:
        pass

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    @abc.abstractmethod
    def __iter__(self) -> Iterator[torch.Tensor]:
        pass

    @abc.abstractmethod
    def batched(self, indices: Iterator[int]) -> Batch:
        """Get the padded data and the original sizes of the data from a list of indices."""


class InMemoryAccessor(DataAccessor):
    """Data accessor where everything is in memory."""

    def __init__(self, indices: dict[int, tuple[int, int]], data: torch.Tensor) -> None:
        self.device = Environment().device
        self.indices = indices
        verify_empty_datapoints(self.indices)
        self.data = data.to(self.device)

    def __repr__(self) -> str:
        return f"InMemoryAccessor(data of shape {tuple(self.data.shape)}, with {len(self)} items)"

    def __getitem__(self, i: int) -> torch.Tensor:
        if i not in self.indices:
            raise IndexError
        start, end = self.indices[i]
        return self.data[start:end]

    def __len__(self) -> int:
        return len(self.indices)

    def __iter__(self) -> Iterator[torch.Tensor]:
        for i in self.indices:
            yield self[i]

    def batched(self, indices: Iterator[int]) -> Batch:
        """Get the padded data and the original sizes of the data from a list of indices."""
        sizes, data = [], []
        for i in indices:
            this_data = self[i]
            sizes.append(this_data.size(0))
            data.append(this_data)
        return Batch(pad_sequence(data, batch_first=True), torch.tensor(sizes, dtype=torch.int64, device=self.device))


def find_all_files(root: str | Path, extension: str) -> dict[str, Path]:
    """Recursively find all files with the given `extension` in `root`."""
    return dict(sorted((p.stem, p) for p in Path(root).rglob(f"*{extension}")))


def normalize_with_singularity(x: torch.Tensor) -> torch.Tensor:
    """Normalize the given vector across the third dimension.

    Extend all vectors by eps=1e-12 to put the null vector at the maximal
    cosine distance from any non-null vector.
    """
    norm_x = (x**2).sum(dim=1, keepdim=True)
    x /= torch.sqrt(norm_x)
    zero_vals = (norm_x == 0).view(x.size(0))
    x[zero_vals] = 1 / math.sqrt(x.size(1))
    border_vect = torch.zeros((x.size(0), 1), dtype=x.dtype, device=x.device) + 1e-12
    border_vect[zero_vals] = -2 * 1e12
    return torch.cat([x, border_vect], dim=1)


def read_item(item: str | Path) -> pl.DataFrame:
    """Read an item file."""
    labels = pl.read_csv(item, separator=" ")
    if set(labels.columns) != {"#file", "onset", "offset", "#phone", "prev-phone", "next-phone", "speaker"}:
        raise ValueError("Invalid item file")
    return labels


def load_data_from_item(
    paths: dict[str, Path],
    labels: pl.DataFrame,
    frequency: int,
    feature_maker: FeatureMaker,
    *,
    normalize: bool = True,
) -> tuple[dict[int, tuple[int, int]], torch.Tensor]:
    """Load all data in memory. Return a dictionary of indices and a tensor of data."""
    metadata = labels[["#file", "onset", "offset"]].with_row_index()
    start = (pl.col("onset") * frequency - 0.5).ceil().cast(pl.Int64).alias("start")
    end = (pl.col("offset") * frequency - 0.5).floor().cast(pl.Int64).alias("end")
    length = (end - start).alias("length")
    right = length.cum_sum().alias("right")
    left = length.cum_sum().shift(1).fill_null(0).alias("left")
    lazy = metadata.lazy().sort("#file", maintain_order=True).with_columns(start, end, left, right)
    indices_lazy = lazy.select("left", "right", "index").sort("index").select("left", "right")
    by_file_lazy = lazy.select("#file", "start", "end").group_by("#file", maintain_order=True).agg("start", "end")
    indices, by_file = pl.collect_all([indices_lazy, by_file_lazy])

    data, device = [], Environment().device
    for fileid, start_indices, end_indices in tqdm(by_file.iter_rows(), desc="Building dataset", total=len(by_file)):
        features = feature_maker(paths[fileid]).detach().to(device)
        if normalize:
            features = normalize_with_singularity(features)
        data += [features[start:end] for start, end in zip(start_indices, end_indices, strict=True)]
    return dict(enumerate(indices.rows())), torch.cat(data, dim=0)


@dataclass(frozen=True)
class Dataset:
    """Simple interface to a dataset.

    :param labels: ``pl.DataFrame`` containing the labels of the datapoints.
    :param accessor: ``DataAccessor`` to access the data.
    """

    labels: pl.DataFrame
    accessor: DataAccessor

    def __repr__(self) -> str:
        return f"labels:\n{self.labels!r}\naccessor: {self.accessor!r}"

    @classmethod
    def from_item(  # noqa: PLR0913
        cls,
        item: str | Path,
        root: str | Path,
        frequency: int,
        feature_maker: FeatureMaker,
        *,
        normalize: bool = True,
        extension: str = ".pt",
    ) -> "Dataset":
        """Create a dataset from an item file."""
        labels = read_item(item)
        paths = find_all_files(root, extension)
        indices, data = load_data_from_item(paths, labels, frequency, feature_maker, normalize=normalize)
        return Dataset(labels=labels, accessor=InMemoryAccessor(indices, data))

    @classmethod
    def from_dataframe(cls, df: SupportsInterchange, feature_columns: str | Collection[str]) -> "Dataset":
        """Create a dataset from a DataFrame (polars or pandas)."""
        df = pl.from_dataframe(df.__dataframe__())
        labels = df.select(cs.exclude(feature_columns))
        indices = {i: (i, i + 1) for i in range(len(labels))}
        data = df.select(feature_columns).cast(pl.Float32).to_torch()
        return Dataset(labels=labels, accessor=InMemoryAccessor(indices, data))

    @classmethod
    def from_csv(cls, path: str | Path, feature_columns: str | Collection[str], *, separator: str = ",") -> "Dataset":
        """Create a dataset from a CSV file."""
        return cls.from_dataframe(pl.read_csv(path, separator=separator), feature_columns)

    @classmethod
    def from_dict(cls, data: Mapping[str, Sequence[object]], feature_columns: str | Collection[str]) -> "Dataset":
        """Create a dataset from a dictionary of sequences."""
        return cls.from_dataframe(pl.from_dict(data), feature_columns)

    @classmethod
    def from_dicts(cls, data: Iterable[dict[str, Any]], feature_columns: str | Collection[str]) -> "Dataset":
        """Create a dataset from a sequence of dictionaries."""
        return cls.from_dataframe(pl.from_dicts(data), feature_columns)

    @classmethod
    def from_numpy(cls, features: ArrayLike, labels: Mapping[str, Sequence[object]]) -> "Dataset":
        """Create a dataset from the features (numpy array) and the labels (dictionary of sequences)."""
        features_df = pl.from_numpy(np.asarray(features))
        labels_df = pl.from_dict(labels)
        if len(features_df) != len(labels_df):
            raise ValueError("features and labels must have the same length")
        return cls.from_dataframe(pl.concat((features_df, labels_df), how="horizontal"), features_df.columns)


def dummy_dataset_from_item(item: str | Path) -> Dataset:
    """To debug."""
    labels = read_item(item).with_columns(pl.lit(0).alias("dummy"))
    return Dataset.from_dataframe(labels, "dummy")
