
class TrainingConfig:
    _n_epochs: int
    _batch_size: int
    _lr_max: float
    _dropout: float
    _train_size: float

    def __init__(self, n_epochs: int = 200, lr_max: float = 1e-4,
                 dropout: float = 0.3, batch_size: int = 20,
                 train_size: float = 0.8):
        if not isinstance(n_epochs, int):
            raise ValueError("n_epochs must be an integer.")
        if not isinstance(lr_max, float):
            raise ValueError("lr_max must be a float.")
        if not isinstance(dropout, float):
            raise ValueError("dropout must be a float.")
        if not isinstance(train_size, float):
            raise ValueError("train_size must be a float.")
        if not isinstance(batch_size, int):
            raise ValueError("batch_size must be an integer.")

        self._n_epochs = n_epochs
        self._lr_max = lr_max
        self._dropout = dropout
        self._batch_size = batch_size
        self._train_size = train_size

    @property
    def n_epochs(self):
        return self._n_epochs

    @property
    def train_size(self):
        return self._train_size

    @property
    def lr_max(self):
        return self._lr_max

    @property
    def dropout(self):
        return self._dropout

    @property
    def batch_size(self):
        return self._batch_size
