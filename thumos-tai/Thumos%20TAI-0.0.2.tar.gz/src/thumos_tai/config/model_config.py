from typing import Union

from src.thumos_tai.types.model_enum import ModelType


class ModelConfig:
    _model_type: Union[str, ModelType]
    _save_path: str

    def __init__(self, model_type: Union[str, ModelType], save_path: str):
        if not isinstance(model_type, (str, ModelType)):
            raise ValueError("model_type must be of type string or ModelType")
        if not isinstance(save_path, str):
            raise ValueError("save_path must be of type string")

        if isinstance(model_type, str):
            if model_type in ModelType.__members__:
                self._model_type = ModelType[model_type]
            else:
                raise ValueError("Invalid model type.")
        else:
            self._model_type = model_type

        self._save_path = save_path

    @property
    def model_type(self):
        return self._model_type

    @property
    def save_path(self):
        return self._save_path

