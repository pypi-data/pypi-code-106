from typing import Any
from typing import Set
from typing import Type
from typing import cast

from tortoise import Model as TortoiseModel
from tortoise.exceptions import ConfigurationError
from tortoise.exceptions import OperationalError
from tortoise.models import MODEL


class Model(TortoiseModel):
    """Tortoise model with autogenerated dataclass-like __repr__ and couple of bugfixes."""

    def __str__(self) -> str:
        if not __debug__:
            return f'{self.__class__.__name__}({self.pk or ""})'

        fields_str = ', '.join(
            f'{k}={v.__repr__()}'
            for k, v in self.__dict__.items()
            if not k.startswith('_')
        )
        return f'{self.__class__.__name__}({fields_str})'

    def __repr__(self) -> str:
        return self.__str__()

    # FIXME: Push upstream, _custom_generated_pk not set in Model._init_from_db
    @classmethod
    def _init_from_db(cls: Type[MODEL], **kwargs: Any) -> MODEL:
        model = super()._init_from_db(**kwargs)  # type: ignore
        model._custom_generated_pk = False
        return cast(MODEL, model)

    # FIXME: Push upstream, fields with has_db_field=False are ignored
    def _set_kwargs(self, kwargs: dict) -> Set[str]:
        meta = self._meta

        # Assign values and do type conversions
        passed_fields = {*kwargs.keys()} | meta.fetch_fields

        for key, value in kwargs.items():
            if key in meta.fk_fields or key in meta.o2o_fields:
                if value and not value._saved_in_db:
                    raise OperationalError(
                        f"You should first call .save() on {value} before referring to it"
                    )
                setattr(self, key, value)
                passed_fields.add(meta.fields_map[key].source_field)
            elif key in meta.backward_fk_fields:
                raise ConfigurationError(
                    "You can't set backward relations through init, change related model instead"
                )
            elif key in meta.backward_o2o_fields:
                raise ConfigurationError(
                    "You can't set backward one to one relations through init,"
                    " change related model instead"
                )
            elif key in meta.m2m_fields:
                raise ConfigurationError(
                    "You can't set m2m relations through init, use m2m_manager instead"
                )
            else:
                field_object = meta.fields_map.get(key)
                if field_object is None:
                    continue
                if field_object.generated:
                    self._custom_generated_pk = True
                if value is None and not field_object.null:
                    raise ValueError(
                        f"{key} is non nullable field, but null was passed"
                    )
                setattr(self, key, field_object.to_python_value(value))

        return passed_fields
