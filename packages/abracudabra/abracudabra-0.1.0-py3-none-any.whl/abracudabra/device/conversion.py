"""Move an array, series, or tensor to a device."""

from __future__ import annotations

from contextlib import nullcontext
from typing import TYPE_CHECKING, Literal, cast, overload

from .._import import get_library_name, raise_library_not_found
from .._validate import Library, validate_obj_type
from .base import Device, DeviceType, _raise_invalid_device_type

if TYPE_CHECKING:
    import cudf
    import pandas as pd
    from torch import Tensor

    from ..annotations import Array, DataFrame, Index, Series


def to_cupy_array(sequence: object, /, device_idx: int | None = None) -> object:
    """Convert a sequence to a cupy array."""
    try:
        import cupy as cp
    except ImportError:  # pragma: no cover
        raise_library_not_found("cupy")

    with cp.cuda.Device(device_idx) if device_idx is not None else nullcontext():
        return cp.asarray(sequence)


def array_to_device(array: object, /, device: Device | str) -> Array:
    """Move a numpy/cupy array to a device."""
    device = Device.parse(device)
    library = get_library_name(array)

    if library == "numpy" and validate_obj_type(array, Library.numpy):
        if device.type == "cpu":
            return array
        elif device.type == "cuda":
            return to_cupy_array(array, device.idx)
        else:
            _raise_invalid_device_type(device.type)

    elif library == "cupy" and validate_obj_type(array, Library.cupy):
        match device.type:
            case "cpu":
                return array.get()
            case "cuda":
                return to_cupy_array(array, device.idx)
            case _:
                _raise_invalid_device_type(device.type)

    else:  # guard
        msg = f"Expected a numpy or cupy array, but got '{type(array).__name__}'."
        raise TypeError(msg)


@overload
def frame_to_device(frame: Index, /, device_type: Literal["cpu"]) -> pd.Index: ...


@overload
def frame_to_device(frame: Index, /, device_type: Literal["cuda"]) -> cudf.Index: ...


@overload
def frame_to_device(frame: Series, /, device_type: Literal["cpu"]) -> pd.Series: ...


@overload
def frame_to_device(frame: Series, /, device_type: Literal["cuda"]) -> cudf.Series: ...


@overload
def frame_to_device(
    frame: DataFrame, /, device_type: Literal["cpu"]
) -> pd.DataFrame: ...


@overload
def frame_to_device(
    frame: DataFrame, /, device_type: Literal["cuda"]
) -> cudf.DataFrame: ...


@overload
def frame_to_device(
    frame: object, /, device_type: DeviceType
) -> Index | Series | DataFrame: ...


def frame_to_device(
    frame: object, /, device_type: DeviceType
) -> Index | Series | DataFrame:
    """Move a pandas/cudf series or dataframe to a device.

    Args:
        frame: The series or dataframe to move.
        device_type: The device type to move the frame to.

    Returns:
        The series or dataframe on the specified device.

    """
    library = get_library_name(frame)

    if library == "pandas" and validate_obj_type(frame, Library.pandas):
        match device_type:
            case "cpu":
                return frame
            case "cuda":
                try:
                    import cudf
                except ImportError:  # pragma: no cover
                    raise_library_not_found("cudf")

                return cast(
                    cudf.Index | cudf.Series | cudf.DataFrame, cudf.from_pandas(frame)
                )
            case _:
                _raise_invalid_device_type(device_type)

    if library == "cudf" and validate_obj_type(frame, Library.cudf):
        match device_type:
            case "cpu":
                return frame.to_pandas()
            case "cuda":
                return frame
            case _:
                _raise_invalid_device_type(device_type)

    msg = (
        "Expected a pandas or cudf series or dataframe, "
        f"but got '{type(frame).__name__}'."
    )
    raise TypeError(msg)


def tensor_to_device(tensor: object, /, device: Device | str) -> Tensor:
    """Move a torch tensor to a device."""
    if get_library_name(tensor) != "torch" or not validate_obj_type(
        tensor, Library.torch
    ):
        msg = f"Expected a torch tensor, but got '{type(tensor)!r}'."
        raise TypeError(msg)

    return tensor.to(Device.parse(device).to_torch())


def to_device(
    sequence: Array | Series | Tensor, /, device: Device | str
) -> Array | Series | Tensor:
    """Move an array, series, or tensor to a device.

    Call the appropriate function to move the element to the device:

    * :py:func:`array_to_device` for numpy/cupy arrays.
    * :py:func:`series_to_device` for pandas/cudf series.
    * :py:func:`tensor_to_device` for torch tensors.

    """
    library = get_library_name(sequence)

    if library in {"numpy", "cupy"}:
        return array_to_device(sequence, device)
    elif library in {"pandas", "cudf"}:
        device = Device.parse(device)
        return frame_to_device(sequence, device.type)
    elif library == "torch":
        return tensor_to_device(sequence, device)
    else:
        msg = (
            "Expected a numpy/cupy array, pandas/cudf series/dataframe, "
            f"or torch tensor, but got '{type(sequence).__name__}'."
        )
        raise TypeError(msg)
