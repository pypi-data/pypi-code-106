from __future__ import annotations
from datetime import date

from dbc.domain.reference import Reference
from dbc.query.query import Query
from dbc.common.constants.query import *


class DatabaseFieldType:
    def __init__(self,
                 type: str,
                 name: str,
                 value: object = None,
                 pk: bool = False,
                 fk: bool = False,
                 references: Reference = None,
                 characters: int = None,
                 nullable: bool = False,
                 unique: bool = False,
                 index: bool = False,
                 options: set = None,
                 signed: bool = False,
                 float_size: int = None,
                 decimal_size: int = None,
                 extra: str = None,
                 default: object = None):
        """
        Base class for SQL field type wrappers.
        :param type: type of field in table.
        :param name: name of field in table.
        :param value: value of this field.
        :param pk: primary key flag.
        :param fk: foreign key flag.
        :param references: field referenced by foreign key.
        :param characters: size of a VarChar field.
        :param nullable: flag to allow nullable fields or not.
        :param unique: flag to enforce uniqueness or not.
        :param index: index flag.
        :param options: set of values for enum fields.
        :param signed: specifies whether a numeric field is signed ot unsigned.
        :param float_size: number of digits in total for a decimal field.
        :param decimal_size: number of digits to the right of decimal for a decimal field.
        :param extra: used to indicate auto increment on an Int field.
        :param default: used to place a default value in if None is given.
        """
        self.type = type
        self.name = name
        self.value = value
        self.pk = pk
        self.fk = fk
        self.references = references
        self.characters = characters
        self.nullable = nullable
        self.unique = unique
        self.index = index
        self.options = options
        self.signed = signed
        self.float_size = float_size
        self.decimal_size = decimal_size
        self.extra = extra
        self.default = default
        self._foreign_field_reference = False

    def set_to_foreign_field(self, foreign_table: str = None, foreign_field: str = None, alias: str = None) -> None:
        self.value = f"{foreign_table}.{foreign_field}" if alias is None else alias
        self._foreign_field_reference = True

    def formatted_value(self, fragment: bool = False):
        """
        Formats the supplied value to be handled by the database.
        :return: appropriate formatted value.
        """
        if isinstance(self.value, str):
            if NULL in self.value or self._foreign_field_reference:
                return self.value
            else:
                if fragment:
                    return f"\"{'%' + self.value + '%'}\""  # for LIKE statements
                else:
                    return f"\"{self.value}\""
        elif isinstance(self.value, Query):
            return f"({self.value.select_statements})"
        elif isinstance(self.value, date):
            return f"\"{self.value.strftime('%Y-%m-%d')}\""
        else:
            return str(self.value) if self.value is not None else NULL

    @property
    def definition(self) -> str:
        field_definition = f"{self.name} {self.type}"
        if self.extra is not None:
            field_definition += f" {self.extra}"
        if self.characters is not None:
            field_definition += f"({self.characters})"
        if self.options is not None:
            field_definition += f"{tuple(option for option in self.options)}"
        field_definition += f" {NULL if self.nullable else NOT_NULL}"
        if self.unique:
            field_definition += f" {UNIQUE}"
        if self.pk:
            field_definition += f" {PRIMARY_KEY}"
        return field_definition

    def __repr__(self) -> str:
        return f"DatabaseField(name={self.name}, type={self.type}, unique={self.unique}, pk={self.pk}, fk={self.fk})"
