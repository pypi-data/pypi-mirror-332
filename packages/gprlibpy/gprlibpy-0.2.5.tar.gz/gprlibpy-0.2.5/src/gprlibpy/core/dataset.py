from __future__ import annotations

import logging
import typing
from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path
import zipfile
from tempfile import TemporaryDirectory
from threading import Thread

import numpy as np
import xarray as xr
from skyio import GenericPath, CloudPath
from tqdm.dask import TqdmCallback

if typing.TYPE_CHECKING:
    from .scan import Scan

logger = logging.getLogger("rich")

class Dataset:
    """
    A class to represent a dataset of GPR data.
    """

    def __init__(self, dataset: xr.Dataset):
        self._xarr_ds = dataset

    @property
    def xarr_ds(self):
        """
        Get the xarray Dataset object
        :return:
        """
        return self._xarr_ds

    def __len__(self):
        """
        Get the length of the dataset object
        :return:
        """
        return len(self._xarr_ds.data_vars)

    def __delitem__(self, key):
        """
        Delete an item from the Dataset object
        :param key: key to delete
        :return: None
        """
        assert key in self._xarr_ds.data_vars, f"Key {key} does not exist"
        self.drop(key)

    def __getitem__(self, key) -> Scan:
        """
        Get the item, all nan values are dropped before returning the Scan object
        :param key: key to get the item
        :return: Scan object
        """
        assert key in self._xarr_ds.data_vars, f"Key {key} does not exist"
        xarr = self._xarr_ds[key]
        from .scan import Scan
        return Scan(xarr)

    def __setitem__(self, key, value):
        """
        Set the item, not implemented for a Dataset object
        :param key: key to set the item
        :param value: value to set the item
        :return: None
        """
        raise NotImplementedError("Cannot set items in a Dataset object")

    def __iter__(self):
        """
        Iterate over the Dataset object
        :return: key, value
        """
        for key in self._xarr_ds.data_vars:
            yield key, self[key]

    def __repr__(self):
        """
        Get the representation of the Dataset object
        :return:
        """
        return self._xarr_ds.__repr__()

    def __str__(self):
        """
        Get the string representation of the Dataset object
        :return:
        """
        return self._xarr_ds.__str__()

    def __contains__(self, item):
        """
        Check if the Dataset object contains a key
        :param item: key
        :return: b1n
        """
        return item in self._xarr_ds.data_vars


    @classmethod
    def from_dict(cls, scans_dict: typing.Dict[str, Scan]) -> Dataset:
        """
        Create a Dataset object from a dictionary of Scan objects
        :param scans_dict: dictionary of Scan objects
        :return: Dataset object
        """
        xarr_ds = xr.merge(
            [v.xarr.rename(k) for k, v in scans_dict.items()],
            join="outer",
            compat="override",
            fill_value=np.nan,
        )
        return cls(xarr_ds)


    @classmethod
    def from_zip(cls, path):
        """
        Create a Dataset object from a path to a zip file
        :param path: path to a zip file
        :return: Dataset object
        """
        from .scan import Scan
        zip_path = GenericPath(path)
        with TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

            data = Scan.from_path(temp_dir, return_dataset=False)
            if not isinstance(data, list):
                data = [data]
            return cls.from_dict({scan.name: scan for scan in data})



    @classmethod
    def from_path(cls, path):
        """
        Create a Dataset object from a path to a zarr file
        :param path: path to a zarr file
        :return: Dataset object
        """
        generic_path = GenericPath(path)
        if isinstance(generic_path, CloudPath):
            return cls.from_uri(path)
        return cls(xr.open_zarr(path))

    @classmethod
    def from_uri(cls, url) -> Dataset:
        """
        Create a Dataset object from a path to a zarr file
        :param url: GCP file URL
        :return:
        """
        store = GenericPath(url).get_mapper(check=False, create=False)
        return cls(xr.open_zarr(store))

    def save(self, file_path : typing.Union[str, Path, GenericPath], **kwargs) -> None:
        """
        Save the Dataset object to a zarr file or GCP bucket
        :param file_path: path to the zarr file or GCP bucket
        :return: None
        """

        file_path = GenericPath(file_path)
        store = file_path.get_mapper()
        write_job = self._xarr_ds.to_zarr(store, compute=False, **kwargs)
        with TqdmCallback(desc="uploading....."):
            write_job.persist()

    def update(self, data_vars: typing.Dict[str, Scan]):
        """
        update variables of a dataset
        :param data_vars:
        :return:
        """
        new_data_vars = {k: v.xarr for k, v in data_vars.items()}
        self._xarr_ds = self._xarr_ds.assign(new_data_vars)

    def drop(self, *keys : str):
        """
        Drop variables from the dataset
        :param keys: list of keys to drop
        :return: None
        """
        self._xarr_ds = self._xarr_ds.drop_vars(keys, errors="ignore")
        for dim in self._xarr_ds.dims:
            self._xarr_ds = self._xarr_ds.dropna(dim=dim, how="all")

