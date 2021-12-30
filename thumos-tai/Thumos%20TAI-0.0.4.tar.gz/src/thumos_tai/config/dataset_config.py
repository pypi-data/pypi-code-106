import os

from thumos_tai.dataset import StockCsvReader
from thumos_tai.dataset.data_reader import DataReader


class DatasetConfig:
    _annotations_path: str
    _samples_dir_path: str
    _data_reader: DataReader

    def __init__(self, annotations_path: str, samples_dir_path: str,
                 data_reader: DataReader = None):
        if not isinstance(annotations_path, str):
            raise ValueError("annotations_path must be of type str")
        if not isinstance(samples_dir_path, str):
            raise ValueError("samples_dir_path must be of type str")
        if not os.path.exists(annotations_path):
            raise FileNotFoundError("annotations_path appears invalid")
        if not os.path.exists(samples_dir_path):
            raise FileNotFoundError(f"samples_dir_path appears invalid: {samples_dir_path}")

        if data_reader is None:
            self._data_reader = StockCsvReader()
        elif not isinstance(data_reader, DataReader):
            raise ValueError("data_reader must be an implementation of DataReader")

        self._annotations_path = annotations_path
        self._samples_dir_path = samples_dir_path

    @property
    def annotations_path(self):
        return self._annotations_path

    @property
    def data_reader(self):
        return self._data_reader

    @property
    def samples_dir_path(self):
        return self._samples_dir_path
