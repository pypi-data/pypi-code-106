from dbc.domain.fields.field import DatabaseFieldType


class Varchar(DatabaseFieldType):
    TYPE = "varchar"

    def __init__(self,
                 name: str,
                 characters: int,
                 value: str = None,
                 nullable: bool = False,
                 pk: bool = False,
                 fk: bool = False,
                 references: DatabaseFieldType = None,
                 unique: bool = False,
                 index: bool = False):
        """
        Field type wrapper for SQL Varchar type.
        :param name: name of field in table.
        :param characters: max number of characters allowed.
        :param value: value of this field.
        :param nullable: flag to allow nullable fields or not.
        :param pk: primary key flag.
        :param fk: foreign key flag.
        :param references: field referenced by foreign key.
        :param unique: flag to enforce uniqueness or not.
        :param index: index flag.
        """
        super().__init__(self.TYPE,
                         name=name,
                         value=value,
                         nullable=nullable,
                         pk=pk,
                         fk=fk,
                         references=references,
                         unique=unique,
                         index=index,
                         characters=characters)
