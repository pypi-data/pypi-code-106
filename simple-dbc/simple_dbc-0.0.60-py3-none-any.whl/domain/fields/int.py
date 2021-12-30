from dbc.domain.fields.field import DatabaseFieldType


class Int(DatabaseFieldType):
    TYPE = "int"

    def __init__(self,
                 name: str, value: int = None,
                 int_type: str = "",
                 signed: bool = False,
                 nullable: bool = False,
                 pk: bool = False,
                 fk: bool = False,
                 references: DatabaseFieldType = None,
                 unique: bool = False,
                 index: bool = False,
                 extra: str = None):
        """
        Field type wrapper for SQL Int type.
        :param name: name of field in table.
        :param value: value of this field.
        :param int_type: type of integer field (e.g, tinyint, smallint, etc).
        :param signed: allows for negative numbers if True, doesn't if False.
        :param nullable: flag to allow nullable fields or not.
        :param pk: primary key flag.
        :param fk: foreign key flag.
        :param references: field referenced by foreign key.
        :param unique: flag to enforce uniqueness or not.
        :param index: index flag.
        """
        super().__init__(type=int_type+Int.TYPE,
                         name=name,
                         value=value,
                         signed=signed,
                         nullable=nullable,
                         pk=pk,
                         fk=fk,
                         references=references,
                         unique=unique,
                         index=index,
                         extra=extra)


class AutoIncrement(Int):
    TYPE = "auto_increment"

    def __init__(self, name: str, pk: bool = False, index: bool = False):
        """
        Field type wrapper for SQL Int type (with auto increment).
        :param name: name of field in table.
        :param pk: primary key flag.
        :param index: index flag.
        """
        super().__init__(name=name, pk=pk, signed=False, index=index, extra=self.TYPE)
