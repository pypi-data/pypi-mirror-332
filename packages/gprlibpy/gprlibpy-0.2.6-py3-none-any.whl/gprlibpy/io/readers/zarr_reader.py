import logging
import typing
from pathlib import Path
import xarray as xr
from lgopy.core import DataReaderFactory, DataReader

logger = logging.getLogger("rich")


@DataReaderFactory.register(".zarr")
class ZarrReader(DataReader):
    """
    Cdf data reader
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, file_path: typing.Union[str, Path]) -> xr.DataArray:
        return xr.open_zarr(file_path).to_array()
