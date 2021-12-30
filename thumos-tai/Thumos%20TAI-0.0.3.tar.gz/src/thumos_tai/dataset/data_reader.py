from abc import ABC
import numpy as np


class DataReader(ABC):
    def read(self, path: str) -> np.ndarray:
        raise NotImplementedError()

