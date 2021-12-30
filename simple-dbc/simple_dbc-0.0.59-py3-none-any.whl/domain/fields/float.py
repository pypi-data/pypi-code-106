from dbc.domain.fields.field import DatabaseFieldType


class Float(DatabaseFieldType):
    TYPE = "float"

    def __init__(self,
                 name: str,
                 value: float = None,
                 float_size: int = None,
                 decimal_size: int = None,
                 nullable: bool = False,
                 pk: bool = False,
                 fk: bool = False,
                 references: DatabaseFieldType = None,
                 unique: bool = False,
                 index: bool = False):
        """
        Field type wrapper for SQL Float type.
        :param name: name of field in table.
        :param value: value of this field.
        :param float_size: number of digits in total (length of integer value PLUS length of decimal value).
        :param decimal_size: number of digits to the right of decimal.
        :param nullable: flag to allow nullable fields or not.
        :param pk: primary key flag.
        :param fk: foreign key flag.
        :param references: field referenced by foreign key.
        :param unique: flag to enforce uniqueness or not.
        :param index: index flag.
        """
        super().__init__(self.TYPE if float_size is None and decimal_size is None else f"decimal({float_size}, {decimal_size})",
                         name=name,
                         value=value,
                         nullable=nullable,
                         pk=pk,
                         fk=fk,
                         references=references,
                         unique=unique,
                         index=index,
                         signed=True,
                         float_size=float_size,
                         decimal_size=decimal_size)
