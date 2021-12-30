from __future__ import annotations
from typing import List

from dbc.query.query import Query
from pydantic import BaseModel, validator


class UniqueIndex(BaseModel):
    name: str
    field_names: List[str]

    @validator('field_names')
    def passwords_match(cls, field_names):
        if len(field_names) < 2:
            raise ValueError('UniqueIndex requires 2 fields or more. A UniqueIndex with one field is a primary key')
        return field_names

    # def difference(self, other: UniqueIndex, table_name: str) -> Query:
    #     query = Query()
    #     if other is not None:
    #         query.drop_unique_index(other.unique_index.name, table_name)
    #     query.create_unique_index(unique_index_name=self.name, unique_index_fields=self.field_names, table_name=table_name)
    #     return query

    def __eq__(self, other: UniqueIndex) -> bool:
        if self.name != other.name:
            return False
        elif self.field_names != other.field_names:
            return False
        else:
            return True

    def __ne__(self, other: UniqueIndex) -> bool:
        return not self.__eq__(other)
