from dbc.domain.fields.field import DatabaseFieldType


class Blob(DatabaseFieldType):
    TYPE = "blob"

    def __init__(self, name: str, value: object = None, nullable: bool = False):
        """
        Field type wrapper for SQL Blob type.
        :param name: name of field in table.
        :param value: value of this field.
        :param nullable: flag to allow nullable fields or not.
        """
        super().__init__(self.TYPE, name=name, value=value, nullable=nullable)
