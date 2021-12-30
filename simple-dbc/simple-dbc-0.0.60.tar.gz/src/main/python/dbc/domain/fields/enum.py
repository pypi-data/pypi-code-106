from dbc.domain.fields.field import DatabaseFieldType


class Enum(DatabaseFieldType):
    TYPE = "enum"

    def __init__(self, name: str, value: str = None, nullable: bool = False, options: list = None):
        """
        Field type wrapper for SQL Enum type.
        :param name: name of field in table.
        :param value: value of this field.
        :param nullable: flag to allow nullable fields or not.
        :param options:
        """
        super().__init__(self.TYPE, name=name, value=value, nullable=nullable, options=options)
