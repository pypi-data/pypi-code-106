import os

import numpy as np
import pandas as pd
from torch.utils.data import Dataset


class StockDataset(Dataset):
    def __init__(self, annotations_file, stock_dir, csv_reader,
                 transform=None, target_transform=None):
        self.stock_labels = pd.read_csv(annotations_file)
        self.stock_dir = stock_dir
        self.transform = transform
        self.target_transform = target_transform
        self.csv_reader = csv_reader

    def __len__(self):
        return len(self.stock_labels)

    def get(self):
        x = []
        y = []
        for i in range(0, self.__len__()):
            current_x, current_y = self.__getitem__(i)
            x.append(current_x)
            y.append(current_y)
        return np.asarray(x), np.asarray(y)

    def __getitem__(self, idx):
        stock_path = self.stock_labels.iloc[idx, 0]
        stock = self.csv_reader.read(stock_path)
        label = self.stock_labels.iloc[idx, 1]
        if self.transform:
            stock = self.transform(stock)
        if self.target_transform:
            label = self.target_transform(label)
        return stock, label

    # def __getitem__(self, idx):
    #     stock_path = os.path.join(self.stock_dir, self.stock_labels.iloc[idx, 0])
    #     stock = self.csv_reader.read(stock_path)
    #     label = self.stock_labels.iloc[idx, 1]
    #
    #     if self.transform:
    #         stock = self.transform(stock)
    #     if self.target_transform:
    #         label = self.target_transform(label)
    #     return stock.float(), label
