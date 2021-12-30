from dbc.domain.fields.field import DatabaseFieldType


class Text(DatabaseFieldType):
    TYPE = "text"

    def __init__(self,
                 name: str,
                 value: str = None,
                 nullable: bool = False,
                 pk: bool = False,
                 fk: bool = False,
                 references: DatabaseFieldType = None,
                 unique: bool = False,
                 index: bool = False):
        """
        Field type wrapper for SQL Text type.
        :param name: name of field in table.
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
                         index=index)
