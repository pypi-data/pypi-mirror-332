"""Query the device of a numpy/cupy array, series or torch tensor."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, overload

from .._import import get_library_name
from .._validate import Library, validate_obj_type
from .base import Device, DeviceType

if TYPE_CHECKING:
    from torch import Tensor

    from ..annotations import Array, DataFrame, Series


def _cupy_get_device(array: object, /) -> Device:
    """Get the device of a cupy array.

    Args:
        array: The array to check.

    Returns:
        The device of the array.

    """
    return Device("cuda", array.device.id)  # type: ignore[attr-defined]


@overload
def frame_get_device_type(
    frame: Series | DataFrame, /, *, raise_if_unknown: Literal[True] = ...
) -> DeviceType: ...


@overload
def frame_get_device_type(
    frame: Series | DataFrame, /, *, raise_if_unknown: bool = ...
) -> DeviceType | None: ...


def frame_get_device_type(
    frame: Series | DataFrame, /, *, raise_if_unknown: bool = True
) -> DeviceType | None:
    """Get the device type of a pandas or cudf series or dataframe."""
    library = get_library_name(frame)

    if library == "pandas" and validate_obj_type(frame, Library.pandas):
        return "cpu"

    if library == "cudf" and validate_obj_type(frame, Library.cudf):
        return "cuda"

    if raise_if_unknown:
        msg = (
            "Expected a pandas/cudf index, series or dataframe, "
            f"but got '{type(frame).__name__}'."
        )
        raise TypeError(msg)

    return None


def _torch_get_device(tensor: Tensor, /) -> Device:
    """Get the device of a torch tensor.

    Args:
        tensor: The tensor to check.

    Returns:
        The device of the tensor.

    """
    device = tensor.device
    return Device.validate(device.type, device.index)


@overload
def get_device(
    element: Array | Tensor, /, *, raise_if_unknown: Literal[True] = ...
) -> Device: ...


@overload
def get_device(
    element: Array | Tensor, /, *, raise_if_unknown: bool = ...
) -> Device | None: ...


def get_device(
    element: Array | Tensor, /, *, raise_if_unknown: bool = True
) -> Device | None:
    """Get the device of a numpy/cupy array or series.

    Args:
        element: The element to check.
        raise_if_unknown: Whether to raise an error if the element is not a known
            array or tensor.

    Returns:
        The device of the element.

    """
    library = get_library_name(element)

    if library == "numpy" and validate_obj_type(element, Library.numpy):
        return Device("cpu")

    if library == "cupy" and validate_obj_type(element, Library.cupy):
        return _cupy_get_device(element)

    if library == "torch" and validate_obj_type(element, Library.torch):
        return _torch_get_device(element)

    if raise_if_unknown:
        msg = (
            "Expected a numpy/cupy array or torch array or tensor, "
            f"but got '{type(element).__name__}'."
        )
        raise TypeError(msg)

    return None


def guess_device(*elements: Array | Tensor, skip_unknown: bool = True) -> Device:
    """Guess the device of a numpy/cupy array or series.

    Args:
        *elements: The elements to check.
        skip_unknown: Whether to skip elements that are not known arrays or tensors.

    Returns:
        The device of the elements.

    Raises:
        ValueError: If no elements are given.
        ValueError: If the elements are on different devices.

    """
    devices = {
        device
        for element in elements
        if (device := get_device(element, raise_if_unknown=not skip_unknown))
        is not None
    }

    if len(devices) == 0:
        msg = "Expected at least one element, but got none."
        raise ValueError(msg)

    if len(devices) > 1:
        msg = (
            f"Expected all elements to be on the same device, "
            f"but found {len(devices)} different devices:"
            + ", ".join(map(repr, devices))
        )
        raise ValueError(msg)

    return devices.pop()
