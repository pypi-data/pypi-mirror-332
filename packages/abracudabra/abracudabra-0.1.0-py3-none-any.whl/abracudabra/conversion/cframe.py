"""Convert to a pandas/cudf series or dataframe."""

from __future__ import annotations

import contextlib
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from ..device.base import Device
from ..device.conversion import to_device
from ..device.library import get_pd_or_cudf
from ..device.query import guess_device
from .carray import to_array

if TYPE_CHECKING:
    from collections.abc import Iterable

    from torch import Tensor

    from ..annotations import Array, DataFrame, Series


def _guess_dataframe_device(
    sequences: Iterable[Tensor | Array],
    /,
    device: str | Device | None = None,
) -> Device:
    """Guess the device of a dataframe."""
    if device is not None:
        return Device.parse(device)

    return guess_device(*sequences, skip_unknown=True)


def to_series(
    sequence: object,
    /,
    index: Array | Tensor | None = None,
    device: str | Device | None = None,
    *,
    strict: bool = False,
    **kwargs: Any,
) -> Series:
    """Convert an array or tensor to a pandas/cudf series.

    Args:
        sequence: The array or tensor to convert.
        index: The optional index for the series.
        device: The device to use for the series.
        strict: Whether to raise an error for unknown data types.
        kwargs: Additional keyword arguments for the series.

    Returns:
        The converted series.

    """
    device = _guess_dataframe_device([sequence], device=device)
    array = to_array(sequence, device=device, strict=strict)

    if index is not None:
        # Try to move the index to the same device as the array
        # If it fails, just pass it as is, and let pandas/cudf handle it
        with contextlib.suppress(TypeError):
            index = to_device(index, device=device)

    pdf_or_cudf = get_pd_or_cudf(device.type)
    return pdf_or_cudf.Series(array, index=index, **kwargs)  # type: ignore[arg-type]


def to_dataframe(
    data: Mapping[str, Array | Tensor] | Tensor | Array,
    /,
    index: Array | Tensor | None = None,
    device: str | Device | None = None,
    *,
    strict: bool = False,
    **kwargs: Any,
) -> DataFrame:
    """Convert to a pandas/cudf dataframe.

    Args:
        data: The data to convert. If a mapping, the keys will be used as column names.
        index: The optional index for the dataframe.
        device: The device to use for the dataframe.
        strict: Whether to raise an error for unknown data types.
        kwargs: Additional keyword arguments for the dataframe.

    Returns:
        The converted dataframe.

    """
    device = _guess_dataframe_device(
        data.values() if isinstance(data, Mapping) else [data],
        device=device,
    )

    if isinstance(data, Mapping):
        data = {
            key: to_array(value, device=device, strict=strict)
            for key, value in data.items()
        }
    else:
        data = to_array(data, device=device, strict=strict)

    if index is not None:
        with contextlib.suppress(TypeError):
            index = to_device(index, device=device)

    df_or_cudf = get_pd_or_cudf(device.type)
    return df_or_cudf.DataFrame(data, index=index, **kwargs)
