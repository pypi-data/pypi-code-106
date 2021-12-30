from typing import List, Optional

from pandaSuit.common.util.list_operations import remove_elements

from dbc.domain.fields.field import DatabaseFieldType
from dbc.domain.index import UniqueIndex


class Table:
    def __init__(self,
                 name: str,
                 unique_index: Optional[UniqueIndex] = None):
        """
        Base class for custom database tables.
        :param name: database table name.
        :param index: table index name.
        :param related_to: external tables referenced by fields of the table.
        :param unique_index: a UniqueIndex composed of two or more fields that must be unique.
        """
        self.name = name
        self.unique_index = unique_index

    def field_names_excluding(self, exclude: list or object, prepend_table_name: bool = True) -> List[str]:
        if prepend_table_name:
            return [f"{self.name}.{field}" for field in remove_elements(self.field_names, exclude)]
        else:
            return remove_elements(self.field_names, exclude)

    @property
    def fields(self) -> List[DatabaseFieldType]:
        """
        Gives all fields of the table object.
        :return: list of field names.
        """
        return [field for field in self.__dict__.values() if isinstance(field, DatabaseFieldType)]

    @property
    def field_names(self) -> List[str]:
        """
        Gives all fields of the table object.
        :return: list of field names.
        """
        return [field.name for field in self.__dict__.values() if isinstance(field, DatabaseFieldType)]

    @property
    def populated_fields(self) -> List[DatabaseFieldType]:
        """
        Gives all field names and corresponding values of the table object.
        :return: dictionary of field, value pairs.
        """
        return [field for field in self.fields if field.value is not None]

    @property
    def unique_keys(self) -> List[DatabaseFieldType]:
        unique_fields = [field for field in self.fields if field.unique]
        if self.primary_key not in unique_fields:
            unique_fields.append(self.primary_key)
        return unique_fields

    @property
    def index(self) -> DatabaseFieldType or None:
        for field in self.fields:
            if field.index:
                return field
        return None

    @property
    def related_to(self) -> list:
        return [field.references.table_name for field in self.fields if field.fk]

    @property
    def foreign_keys(self) -> List[DatabaseFieldType]:
        return [field for field in self.fields if field.fk]

    @property
    def has_foreign_keys(self) -> bool:
        return len(self.foreign_keys) > 0

    @property
    def primary_key(self) -> DatabaseFieldType:
        for field in self.fields:
            if field.pk:
                return field
