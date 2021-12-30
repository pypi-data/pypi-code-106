from dbc.domain.fields.field import DatabaseFieldType


class Date(DatabaseFieldType):
    TYPE = "date"

    def __init__(self, name: str, value: str = None, nullable: bool = False):
        """
        Field type wrapper for SQL Datetime type.
        :param name: name of field in table.
        :param value: date of transaction (yyyy-mm-dd).
        :param nullable: flag to allow nullable fields or not.
        """
        super().__init__(self.TYPE, name=name, value=value, nullable=nullable)
