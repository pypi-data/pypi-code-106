from pathlib import Path

import torch
from fastai.data.transforms import Categorize
from fastai.learner import Learner
from fastai.losses import LabelSmoothingCrossEntropyFlat
from fastai.metrics import RocAucBinary, accuracy
from torch import nn
from tsai.data.core import TSDatasets, TSDataLoaders
from tsai.data.preprocessing import TSStandardize
from tsai.data.validation import get_splits
from tsai.imports import computer_setup
from tsai.models.TST import TST
from tsai.models.XCM import XCM

from thumos_tai.config.dataset_config import DatasetConfig
from thumos_tai.config.model_config import ModelConfig
from thumos_tai.config.training_config import TrainingConfig
from thumos_tai.dataset.stock_dataset import StockDataset
from thumos_tai.dataset.synthetic_generator import SyntheticGenerator
from thumos_tai.types.model_enum import ModelType


class TsaiController:
    def __init__(self, training_config: TrainingConfig = None,
                 model_config: ModelConfig = None,
                 dataset_config: DatasetConfig = None,
                 plot: bool = True):

        self.plot = plot
        self.dataloader = None

        # Dataset
        self.data_reader = dataset_config.data_reader
        self.ANNOTATION_FILE_PATH = dataset_config.annotations_path
        self.SAMPLES_DIR_PATH = dataset_config.samples_dir_path

        # Model
        self.model_type = model_config.model_type
        self.SAVE_PATH = model_config.save_path

        # Training
        self.dropout = training_config.dropout
        self.lr_max = training_config.lr_max
        self.n_epochs = training_config.n_epochs
        self.batch_size = training_config.batch_size
        self.train_size = training_config.train_size

        # Controller setup
        self.random_state = 2
        computer_setup()

    def generate_synthetic_data(self, n_samples: int, sample_length: int):
        Path(self.SAMPLES_DIR_PATH).mkdir(parents=True, exist_ok=True)
        annotations_file = Path(self.ANNOTATION_FILE_PATH)
        annotations_file.parent.mkdir(exist_ok=True, parents=True)

        generator = SyntheticGenerator(self.ANNOTATION_FILE_PATH,
                                       self.SAMPLES_DIR_PATH,
                                       n_samples, sample_length)
        generator.run()
        return self

    def prepare_dataset(self):
        dataset = StockDataset(self.ANNOTATION_FILE_PATH,
                               self.SAMPLES_DIR_PATH,
                               self.data_reader)
        X, y = dataset.get()
        splits = get_splits(y, valid_size=1 - self.train_size, stratify=True,
                            random_state=self.random_state, shuffle=True)
        transforms = [None, [Categorize()]]
        datasets = TSDatasets(X, y, tfms=transforms, splits=splits)
        self.dataloader = TSDataLoaders.from_dsets(datasets.train, datasets.valid, bs=self.batch_size,
                                                   batch_tfms=TSStandardize(by_var=True))
        return self

    def __prepare_model__(self) -> nn.Module:
        if self.model_type is ModelType.TST:
            return TST(self.dataloader.vars, self.dataloader.c, self.dataloader.len, dropout=self.dropout)
        if self.model_type is ModelType.XCM:
            return XCM(self.dataloader.vars, self.dataloader.c, self.dataloader.len)

    def train(self, model: nn.Module = None):
        if self.dataloader is None:
            raise Exception("prepare_dataset method needs to have been called prior.")
        if model is None:
            model = self.__prepare_model__()
        learn = Learner(self.dataloader, model, loss_func=LabelSmoothingCrossEntropyFlat(),
                        metrics=[RocAucBinary(), accuracy])
        learn.fit_one_cycle(self.n_epochs, lr_max=self.lr_max)
        if self.plot and hasattr(learn, "plot_metrics"):
            learn.plot_metrics()
        torch.save(model.state_dict(), self.SAVE_PATH)
