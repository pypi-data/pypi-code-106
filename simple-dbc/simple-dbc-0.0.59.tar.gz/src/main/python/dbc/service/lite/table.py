from __future__ import annotations
from typing import List, Optional

from pydantic import BaseModel

from dbc.service.lite.field import Field
from dbc.service.lite.index import UniqueIndex
from dbc.query.query import Query
from dbc.common.constants.query import AFTER, FIRST


class Table(BaseModel):
    name: str
    table_fields: List[Field]
    unique_index: Optional[UniqueIndex]

    @property
    def foreign_keys(self) -> List[Field]:
        return [field for field in self.table_fields if field.fk]

    @property
    def has_foreign_keys(self) -> bool:
        return any(field.fk for field in self.table_fields)

    @property
    def related_to(self) -> list:
        return [field.references.table_name for field in self.table_fields if field.fk]

    @property
    def index(self) -> Field or None:
        for field in self.table_fields:
            if field.index:
                return field
        return None

    @property
    def primary_key(self) -> Field:
        for field in self.table_fields:
            if field.pk:
                return field

    @property
    def field_mapping(self) -> dict:
        return {table_field.name: table_field for table_field in self.table_fields}

    def difference(self, other: Table) -> List[Query]:
        queries = []
        if len(self.table_fields) != len(other.table_fields) or any(field not in self.table_fields for field in other.table_fields):
            queries += self._fields_diff(other.table_fields)
        if (self.unique_index is None and other.unique_index is not None) or \
                (self.unique_index is not None and other.unique_index is None) or \
                self.unique_index != other.unique_index:
            queries.append(self._unique_index_diff(other.unique_index))
        return queries

    def _fields_diff(self, table_fields: List[Field]) -> List[Query]:
        queries, last_field_name = [], None
        other_fields_dict = {other_field.name: other_field for other_field in table_fields}
        for field in self.table_fields:
            if field.name not in other_fields_dict:
                query = Query()
                query.add_field(field.name,
                                table_name=self.name,
                                position=FIRST if last_field_name is None else f"{AFTER} {last_field_name}")
                queries.append(query)
            elif field != other_fields_dict.get(field.name):
                queries.append(field.difference(other_fields_dict.get(field.name), self.name))
            last_field_name = field.name
        return queries

    def _unique_index_diff(self, other: UniqueIndex or None) -> Query:
        query = Query()
        if other is not None and other.unique_index is not None:
            query.drop_unique_index(other.unique_index.name, self.name)
        query.create_unique_index(unique_index_name=self.unique_index.name,
                                  unique_index_fields=self.unique_index.field_names,
                                  table_name=self.name)
        return query

    def __eq__(self, other: Table) -> bool:
        if self.name != other.name:
            return False
        elif (self.index is None and other.index is not None) or (self.index is not None and other.index is None):
            return False
        elif self.index != other.index and not (self.index is None and other.index is None):
            return False
        elif (self.related_to is None and other.related_to is not None) or (self.related_to is not None and other.related_to is None):
            return False
        elif self.related_to is not None and other.related_to is not None and sorted(self.related_to) != sorted(other.related_to):
            return False
        elif (self.unique_index is None and other.unique_index is not None) or (self.unique_index is not None and other.unique_index is None):
            return False
        elif self.unique_index != other.unique_index and not (self.unique_index is None and other.unique_index is None):
            return False
        elif len(self.table_fields) != len(other.table_fields):
            return False
        else:
            for field in other.table_fields:
                if field.name not in self.field_mapping:
                    return False
                elif field != self.field_mapping.get(field.name):
                    return False
            return True

    def __ne__(self, other: Table) -> bool:
        return not self.__eq__(other)
