import os.path
import random


class SyntheticGenerator:
    annotation_file: str
    sample_dir: str
    n_samples: int
    sample_length: int

    def __init__(self, annotations_file: str,
                 sample_dir: str, n_samples: int,
                 sample_length: int):
        self.sample_dir = sample_dir
        self.annotation_file = annotations_file
        self.n_samples = n_samples
        self.sample_length = sample_length

        with open(annotations_file, 'w') as f:
            f.write("name, label\n")

    def run(self):
        gen_synthetic_dataset(self.sample_dir, self.annotation_file,
                              self.n_samples, self.sample_length)


def gen_synthetic_dataset(out_dir: str, annotations_file: str, n_samples, sample_length):
    with open(annotations_file, 'w') as f:
        f.write("name, label\n")
        for i in range(0, n_samples):
            file_path = os.path.join(out_dir, f"{i}.csv")
            gen_synthetic(file_path, random.uniform(10, 50), sample_length)
            f.write(f"{file_path},{random.randrange(0, 2)}\n")


def gen_synthetic(out_path, start_open: float, length: int):
    with open(out_path, 'w') as f:
        f.write('date, open, close, volume\n')
        stock_open = start_open
        close = stock_open
        for i in range(0, length):
            stock_open = abs(stock_open * random.uniform(0.5, 1.5))
            close = abs(close * random.uniform(0.5, 1.5))
            volume = abs(random.uniform(0.5, 10) * 100)
            f.write(f'1900-01-01, {stock_open}, {close}, {volume}\n')
