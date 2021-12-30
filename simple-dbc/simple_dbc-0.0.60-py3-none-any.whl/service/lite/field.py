from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from dbc.query.query import Query
from dbc.domain.reference import Reference
from dbc.common.constants.query import NULL, NOT_NULL, UNIQUE, PRIMARY_KEY


class Field(BaseModel):
    type: str
    name: str
    value: Optional[object] = None
    pk: Optional[bool] = False
    fk: Optional[bool] = False
    _fk_constraint_name: Optional[str] = None
    references: Optional[Reference] = None
    characters: Optional[int] = None
    nullable: Optional[bool] = False
    unique: Optional[bool] = False
    index: Optional[bool] = False
    options: Optional[set] = None
    signed: Optional[bool] = False
    float_size: Optional[int] = None
    decimal_size: Optional[int] = None
    extra: Optional[str] = None
    default: Optional[object] = None

    class Config:
        arbitrary_types_allowed = True

    def difference(self, other: Field, table_name: str) -> Query:
        query = Query()
        if self.type != other.type:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.nullable != other.nullable:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.unique != other.unique:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.options != other.options:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.signed != other.signed:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.float_size != other.float_size:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.decimal_size != other.decimal_size:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.extra != other.extra:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.default != other.default:
            query.modify_column(field_definition=self.definition, table_name=table_name)
        if self.pk != other.pk:
            query.drop_primary_key(table_name)
            query.add_primary_key(self.name, table_name)
        if self.fk != other.fk:
            if other.fk:
                query.drop_foreign_key(self._fk_constraint_name, table_name)
            if self.fk:
                query.add_foreign_key(field_name=self.name,
                                      referenced_table_name=self.references.table_name,
                                      referenced_field=self.references.field_name,
                                      table_name=table_name)
        if self.characters != other.characters and not (self.characters is None and other.characters is None):
            query.modify_allowable_characters(field_name=self.name, characters=str(self.characters), table_name=table_name)
        if self.index != other.index:
            if self.index is None:
                query.drop_unique_index(index_name=self.name, table_name=table_name)
            else:
                query.add_index(index_name=self.name, field_name=self.name, table_name=table_name)
        return query

    @property
    def definition(self) -> str:
        field_definition = f"{self.name}"
        if self.type == "float" and (self.decimal_size is not None or self.float_size is not None):
            field_definition += f" decimal({self.float_size}, {self.decimal_size})"
        else:
            field_definition += f" {self.type}"
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

    def __eq__(self, other: Field) -> bool:
        for attribute_name, attribute_value in self.__dict__.items():
            if attribute_name in other.__dict__:
                if attribute_value is None:
                    if other.__dict__.get(attribute_name) is not None:
                        return False
                else:
                    if attribute_value != other.__dict__.get(attribute_name):
                        return False
            else:
                return False
        return True

    def __ne__(self, other: Field) -> bool:
        return not self.__eq__(other)

    def __str__(self):
        return f"Field(name={self.name})"
