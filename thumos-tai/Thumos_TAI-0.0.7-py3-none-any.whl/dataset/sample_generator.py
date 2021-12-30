import os
from typing import List

import numpy as np
import pandas as pd

from thumos_tai.types.transform import Transform


def _save_sample(df: pd.DataFrame, path: str) -> None:
    if df is None:
        raise ValueError("Argument df is None.")
    if path is None:
        raise ValueError("Argument path is None.")
    if not isinstance(df, pd.Dataframe):
        raise ValueError("Argument df must be of type pandas.Dataframe")
    if not isinstance(path, str):
        raise ValueError("Argument path must be of type str")

    df.to_csv(path)


class SampleGenerator:
    stock_dir: str
    annotation_file: str
    sample_dir: str
    return_criteria: float
    max_samples_per_stock: int
    transforms: List[Transform]

    def __init__(self, stock_dir: str, annotations_file: str,
                 sample_dir: str, return_criteria: float,
                 max_samples_per_stock: int = None,
                 transforms: List[Transform] = None):
        self.sample_dir = sample_dir
        self.stock_dir = stock_dir
        self.annotation_file = annotations_file
        self.return_criteria = return_criteria
        self.max_samples_per_stock = max_samples_per_stock
        self.current_sample_index = 0
        self.transforms = transforms if transforms else []

        with open(annotations_file, 'w') as f:
            f.write("name, label\n")

    def run(self):
        for root, d, f in os.walk(self.stock_dir):
            for file in f:
                if '.csv' in file:
                    file_path = os.path.join(root, file)
                    df = pd.read_csv(file_path)
                    for transform in self.transforms:
                        transform.perform(df)

                    n_positive_samples = self.analyze_positives(df)
                    self.analyze_negatives(df, n_positive_samples)

    def analyze_negatives(self, df: pd.DataFrame, max_samples: int):
        if max_samples < 1:
            return
        df["Returns"] = df["Close"].pct_change()
        small_return_idxs = np.where(df["Returns"] < 0.2)[0]

        if len(small_return_idxs) < 1:
            return

        max_size = min(max_samples, len(small_return_idxs))
        randomized_samples_indices = np.random.choice(small_return_idxs, size=max_size,
                                                      replace=False)

        negatives: List[str] = []
        for randomized_index in randomized_samples_indices:
            if randomized_index - 30 >= 0:
                sub_df = df[randomized_index - 30:randomized_index]
                sample_path = os.path.join(self.sample_dir, f"{self.current_sample_index}.csv")
                sub_df.to_csv(sample_path)
                self.current_sample_index += 1
                negatives.append(sample_path)

        with open(self.annotation_file, 'a') as f:
            for item in negatives:
                f.write(f"{item},0\n")

    def analyze_positives(self, df: pd.DataFrame) -> int:
        n_positive_samples = 0
        df["Returns"] = df["Close"].pct_change()
        big_return_idxs = np.where(df["Returns"] >= 0.2)[0]

        if len(big_return_idxs) < 1:
            return 0

        positives: List[str] = []
        for i in big_return_idxs:
            if self.max_samples_per_stock is not None and \
                    n_positive_samples >= (self.max_samples_per_stock / 2):
                break
            if i - 30 >= 0:
                sub_df = df[i - 30:i]
                sample_path = os.path.join(self.sample_dir, f"{self.current_sample_index}.csv")
                sub_df.to_csv(sample_path)
                self.current_sample_index += 1
                n_positive_samples += 1
                positives.append(sample_path)

        with open(self.annotation_file, 'a') as f:
            for item in positives:
                f.write(f"{item},1\n")
        return n_positive_samples


if __name__ == "__main__":
    g = SampleGenerator("/home/t/PycharmProjects/breakoutfinder/output",
                        "/test/resources/annotations.csv",
                        "/home/t/PycharmProjects/Thumos TAI/test/samples",
                        return_criteria=0.2)
    g.run()
