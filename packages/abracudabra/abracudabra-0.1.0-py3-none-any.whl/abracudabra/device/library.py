"""Library import functions for device types."""

from types import ModuleType

from .._import import import_library
from .base import DeviceType

_DEVICE_TO_LIBRARY: dict[str, dict[DeviceType, str]] = {
    "array": {"cpu": "numpy", "cuda": "cupy"},
    "frame": {"cpu": "pandas", "cuda": "cudf"},
}
"""A collection of mappings from device types to library names."""

_DEFAULT_DEVICE_TYPE: DeviceType = "cpu"
"""The default device type, if the device type is not specified."""


def _import_library(obj_name: str, device_type: DeviceType | None = None) -> ModuleType:
    if device_type is None:
        device_type = _DEFAULT_DEVICE_TYPE
    library_name = _DEVICE_TO_LIBRARY[obj_name][device_type]
    return import_library(library_name)


def get_np_or_cp(device_type: DeviceType | None = None) -> ModuleType:
    """Get the numpy or cupy library based on the device type."""
    return _import_library("array", device_type)


def get_pd_or_cudf(device_type: DeviceType | None = None) -> ModuleType:
    """Get the pandas or cudf library based on the device type."""
    return _import_library("frame", device_type)
