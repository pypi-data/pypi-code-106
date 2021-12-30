from __future__ import annotations

from pydantic import BaseModel


class Reference(BaseModel):
    table_name: str
    field_name: str

    def __repr__(self):
        return f"{self.table_name}.{self.field_name}"

    def __eq__(self, other: Reference):
        return self.table_name.lower() == other.table_name.lower() and self.field_name.lower() == other.field_name.lower()

    def __ne__(self, other: Reference):
        return not self.__eq__(other)
