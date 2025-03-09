"""Type aliases for numpy, pandas, and cudf objects."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import cudf
    import numpy.typing as npt
    import pandas as pd

    # NB: cupy typing not available
    Array: TypeAlias = npt.NDArray[Any] | Any
    """Type alias for numpy/cupy array."""

    Series: TypeAlias = pd.Series[Any] | cudf.Series
    """Type alias for pandas/cudf series."""

    DataFrame: TypeAlias = pd.DataFrame | cudf.DataFrame
    """Type alias for pandas/cudf dataframe."""

    Index: TypeAlias = pd.Index | cudf.Index
    """Type alias for pandas/cudf index."""
