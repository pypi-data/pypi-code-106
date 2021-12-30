from abc import ABC

import pandas as pd


class Transform(ABC):
    def perform(self, df: pd.DataFrame) -> None:
        raise NotImplementedError()
