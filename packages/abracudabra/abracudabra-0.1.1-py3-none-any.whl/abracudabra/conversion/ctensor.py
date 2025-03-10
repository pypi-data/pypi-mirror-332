"""Convert to Torch tensor."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .._import import get_library_name, raise_library_not_found
from .._validate import Library, validate_obj_type
from ..device.base import Device
from ..device.conversion import tensor_to_device

if TYPE_CHECKING:
    from torch import Tensor

    from .._annotations import Array, DataFrame, Series


def _to_tensor(
    sequence: Array | Series | DataFrame | Tensor, /, *, strict: bool = False
) -> Tensor:
    """Convert an array, series, or dataframe to a Torch tensor.

    The device of the tensor is determined by the device of the input.
    """
    try:
        import torch
    except ImportError:  # pragma: no cover
        raise_library_not_found("torch")

    from torch.utils.dlpack import from_dlpack

    library = get_library_name(sequence)

    # First convert the sequence to a Torch tensor
    if library == "torch" and validate_obj_type(sequence, Library.torch):
        return sequence

    elif library == "numpy" and validate_obj_type(sequence, Library.numpy):
        return torch.from_numpy(sequence)

    elif library == "cupy" and validate_obj_type(sequence, Library.cupy):
        return from_dlpack(sequence)

    elif library == "pandas" and validate_obj_type(sequence, Library.pandas):
        return torch.from_numpy(sequence.to_numpy())

    elif library == "cudf" and validate_obj_type(sequence, Library.cudf):
        return from_dlpack(sequence.to_dlpack())

    if strict:
        msg = (
            f"Expected a NumPy/CuPy array, Pandas/cuDF series or dataframe, "
            f"or Torch tensor, but got '{type(sequence)!r}'."
        )
        raise TypeError(msg)

    # hope for the best
    return torch.as_tensor(sequence)


def to_tensor(
    sequence: Array | Series | Tensor,
    /,
    device: Device | str | None = None,
    *,
    strict: bool = False,
) -> Tensor:
    """Convert an array, series, or dataframe to a Torch tensor.

    Args:
        sequence: The sequence to convert.
        device: The device to convert the sequence to. If None, the sequence stays
            on the same device.
        strict: Whether to raise an error if the sequence is not a valid type.
            A NumPy/CuPy array, Pandas/cuDF series or dataframe, or Torch tensor
            are valid types.
            If False, the sequence is converted to a Torch tensor if possible,
            but it might raise an error if the conversion is not possible.

    Returns:
        A Torch tensor.

    Raises:
        TypeError: If the sequence is not a valid type and ``strict`` is True.

    Examples:
        Build a Torch tensor from a sequence

        >>> import torch
        >>> to_tensor([1, 2, 3])
        tensor([1, 2, 3])

        Build a Torch tensor from a CuPy array

        >>> import cupy as cp
        >>> cupy_array = cp.array([4, 5, 6])
        >>> torch_tensor = to_tensor(cupy_array)
        >>> print(torch_tensor.device)
        tensor([4, 5, 6], device='cuda:0')

    """
    tensor = _to_tensor(sequence, strict=strict)

    if device is not None:
        device = Device.parse(device)
        tensor = tensor_to_device(tensor, device)

    return tensor
