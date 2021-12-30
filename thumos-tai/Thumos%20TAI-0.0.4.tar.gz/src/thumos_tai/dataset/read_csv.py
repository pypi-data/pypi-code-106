import numpy as np
import pandas as pd

from thumos_tai.dataset.data_reader import DataReader


class StockCsvReader(DataReader):
    def __init__(self, delimiter: str = ',', date_row: str = 'Date',
                 close: str = "Close", open: str = "Open", high: str = "High",
                 low: str = "Low", volume: str = "Volume", stock_returns: str = "Returns"):
        self.delimiter = delimiter
        self.date_row = date_row
        self.close = close
        self.open = open
        self.low = low
        self.high = high
        self.volume = volume
        self.stock_returns = stock_returns

    def read(self, path: str) -> np.ndarray:
        df = pd.read_csv(path, sep=self.delimiter)
        df = df.drop(self.date_row, axis=1)
        df = df[[self.close, self.open, self.low, self.high, self.volume, self.stock_returns]]
        df = df.astype(np.float64)
        df = df.fillna(0)
        return np.transpose(df.values)
