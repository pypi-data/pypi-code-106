from dbc.common.constants.query import *


class Query:
    def __init__(self):
        """
        Query class constructs MySQL queries through method calls and dbc-specific conventions.
        """
        self._statements = []

    @staticmethod
    def _create(obj: str, name: str, if_not_exists: bool = False) -> str:
        """
        constructs CREATE statement
        :param obj: type of object to create (e.g. Database, Table, etc.)
        :param name: name of the object to create
        """
        try:
            if if_not_exists:
                return f"{CREATE} {CREATABLE_OBJECTS[obj.upper()]} {IF_NOT_EXISTS} {name}"
            else:
                return f"{CREATE} {CREATABLE_OBJECTS[obj.upper()]} {name}"
        except KeyError:
            print(f"Cannot create a(n) {obj}")

    def create_database(self, name: str) -> None:
        """
        constructs CREATE DATABASE statement
        :param name: name of the database to create
        """
        self._statements.append(self._create(DATABASE, name))

    def create_table(self,
                     table_name: str,
                     table_fields: list,
                     foreign_keys: list,
                     unique_index,
                     index: str) -> None:
        """
        constructs CREATE TABLE statement
        """
        # noinspection PyListCreation
        staging_query = []

        # CREATE TABLE statement
        create_statement = self._create(TABLE, table_name, if_not_exists=True)
        staging_query.append(create_statement)

        # field definitions
        field_definitions = f"({', '.join(field.definition for field in table_fields)}"
        staging_query.append(f"{field_definitions}")

        # foreign key definitions
        if len(foreign_keys) > 0:
            foreign_key_definitions = ", ".join(self._create_foreign_key_definition(
                fk_name=fk.name, fk_reference=fk.references.field_name, referenced_table_name=fk.references.table_name
            ) for fk in foreign_keys)
            staging_query.append(f",{foreign_key_definitions}")

        # add CREATE INDEX query if one is defined for the Table
        # if index is not None:
        #     self.create_index(index_name=index, table_name=table_name)

        # add CREATE UNIQUE INDEX query if one is defined for the Table
        if unique_index is not None:
            staging_query.append(f", {CONSTRAINT} {unique_index.name} {UNIQUE} ({', '.join(unique_index.field_names)})")

        # assemble the full CREATE TABLE query by joining with space delimiters
        self._statements.append(f"{' '.join(staging_query)})")

    def create_tables(self, tables: list) -> None:
        """
        constructs multiple CREATE TABLE statements
        :param tables: Tables to create
        """
        for table in tables:
            self.create_table(table_name=table.name,
                              table_fields=table.table_fields,
                              foreign_keys=table.foreign_keys,
                              unique_index=table.unique_index,
                              index=table.index.name)

    def add_field(self, field_definition: str, table_name: str, position: str = None) -> None:
        alter_table_statement = self._alter_table(table_name)
        add_column_statement = f"{ADD} {COLUMN} {field_definition}"
        if position is not None:
            add_column_statement += f" {FIRST}" if position == FIRST else f" {AFTER} {position}"
        self._statements.append(f"{alter_table_statement} {add_column_statement}")

    @staticmethod
    def _alter_table(table_name: str) -> str:
        """
        constructs ALTER TABLE statement
        """
        return f"{ALTER} {TABLE} {table_name}"

    @staticmethod
    def _create_foreign_key_definition(fk_name: str, fk_reference: str, referenced_table_name: str) -> str:
        return f"{FOREIGN_KEY} ({fk_name}) {REFERENCES} {referenced_table_name}({fk_reference})"

    def create_index(self, index_name: str, table_name: str) -> None:
        create_statement = self._create(INDEX, index_name)
        self._statements.append(f"{create_statement} {ON} {table_name}({index_name})")

    def create_unique_index(self, unique_index_name: str, unique_index_fields: list, table_name: str) -> None:
        alter_table = self._alter_table(table_name)
        create_statement = self._create(UNIQUE_INDEX, unique_index_name)
        on_clause = f" {ON} {table_name} ({', '.join(unique_index_fields)})"
        self._statements.append(alter_table + " " + create_statement + on_clause)

    def drop_unique_index(self, index_name: str, table_name: str) -> None:
        self._statements.append(f"{self._alter_table(table_name)} {self._drop(INDEX, index_name)}")

    def add_index(self, index_name: str, field_name: str, table_name: str) -> None:
        alter_table_statement = self._alter_table(table_name)
        add_index_statement = f"{ADD} {INDEX} {index_name} ({field_name})"
        self._statements.append(f"{alter_table_statement} {add_index_statement}")

    def drop_primary_key(self, table_name: str) -> None:
        alter_table_statement = self._alter_table(table_name)
        self._statements.append(f"{alter_table_statement} {DROP} {PRIMARY_KEY}")

    def add_primary_key(self, field_name: str, table_name: str) -> None:
        alter_table_statement = self._alter_table(table_name)
        self._statements.append(f"{alter_table_statement} {ADD} {PRIMARY_KEY}({field_name})")

    def add_foreign_key(self, field_name: str, referenced_table_name: str, referenced_field: str, table_name: str) -> None:
        alter_table_statement = self._alter_table(table_name)
        add_fk_statement = f"{ADD} {FOREIGN_KEY} {field_name} {REFERENCES} {referenced_table_name}({referenced_field})"
        self._statements.append(f"{alter_table_statement} {add_fk_statement}")

    def drop_foreign_key(self, constraint_name: str, table_name: str) -> None:
        alter_table_statement = self._alter_table(table_name)
        drop_fk_statement = f"{DROP} {FOREIGN_KEY} {constraint_name}"
        self._statements.append(f"{alter_table_statement} {drop_fk_statement}")

    def modify_allowable_characters(self, field_name: str, characters: str, table_name: str) -> None:
        alter_table_statement = self._alter_table(table_name)
        alter_characters_statement = f"{MODIFY} {COLUMN} {field_name} {VARCHAR}({characters})"
        self._statements.append(f"{alter_table_statement} {alter_characters_statement}")

    def _drop(self, obj: str, name: str) -> None:
        """
        constructs DROP statement
        :param obj: type of object to drop (e.g. Database, Table, etc.)
        :param name: name of the object to drop
        """
        try:
            self._statements.append(f"{DROP} {CREATABLE_OBJECTS[obj.upper()]} {name}")
        except KeyError:
            print(f"Cannot drop a {obj}")

    def drop_database(self, name: str) -> None:
        """
        constructs DROP DATABASE statement
        :param name: name of the database to drop
        """
        self._drop(DATABASE, name)

    def drop_table(self, name: str) -> None:
        """
        constructs DROP TABLE statement
        :param name: name of the table to drop
        """
        self._drop(TABLE, name)

    def _show(self, obj: str) -> None:
        """
        constructs SHOW statement
        :param obj: type of object to show (e.g. Database, Table, etc.)
        """
        self._statements.append(f"{SHOW} {obj}")

    def show_databases(self) -> None:
        """
        constructs SHOW DATABASES statement
        """
        self._show(DATABASES)

    def show_tables(self) -> None:
        """
        constructs SHOW TABLES statement
        """
        self._show(TABLES)

    def show_create_table(self, table_name: str) -> None:
        """
        constructs SHOW CREATE TABLE statement
        """
        self._show(f"{CREATE} {TABLE} {table_name}")

    def show_index(self, table_name: str) -> None:
        """
        constructs SHOW INDEX statement
        """
        self._show(f"{INDEX} {FROM} {table_name}")

    def describe_table(self, table_name: str) -> None:
        """
        constructs DESCRIBE TABLE statement
        """
        self._statements.append(f"{DESCRIBE} {table_name}")

    def modify_column(self, field_definition: str, table_name: str) -> None:
        """
        constructs MODIFY COLUMN clause statement
        """
        alter_table_statement = self._alter_table(table_name)
        modify_column_statement = f"{MODIFY} {COLUMN} {field_definition}"
        self._statements.append(f"{alter_table_statement} {modify_column_statement}")

    def delete(self, from_table: str) -> None:
        self._statements.append(f"{DELETE} {FROM} {from_table}")

    def _insert(self, fields: list, into_table: str, external: dict) -> str:
        insert_statement = f"{INSERT} {INTO} {into_table} ({', '.join([field.name for field in fields])}) "
        if external is None:
            insert_statement += f" {VALUES} ({', '.join([field.formatted_value() for field in fields])})"
        else:
            select_statement = self._select(fields=[field.formatted_value() for field in fields],
                                            from_table=', '.join(list(external.keys())))
            insert_statement += select_statement
        return insert_statement

    def insert(self, fields: list, into_table: str, external: dict = None) -> None:
        """
        constructs INSERT statement
        """
        self._statements.append(self._insert(fields, into_table, external))

    @staticmethod
    def _update(fields: list, into_table: str, upsert: bool = False, external: dict = None) -> str:
        sets = ', '.join([f"{field.name}={field.formatted_value()}" for field in fields])
        if upsert:
            update_statement = f"{UPDATE} {sets}"
        else:
            update_statement = f"{UPDATE} {into_table} {SET} {sets}"
        return update_statement

    def update(self, fields: list, into_table: str, external: dict = None) -> None:
        """
        constructs UPDATE statement
        """
        self._statements.append(self._update(fields, into_table, upsert=False, external=external))

    def upsert(self, fields: list, into_table: str, external: dict = None) -> None:
        """
        constructs UPSERT statement
        """
        insert_statement = self._insert(fields, into_table, external)
        insert_statement += f" {ON_DUPLICATE_KEY} "
        update_statement = self._update(fields, into_table, upsert=True, external=external)
        upsert_statement = insert_statement + update_statement
        self._statements.append(upsert_statement)

    @staticmethod
    def _select(from_table: str, fields: list = None, count: bool = False) -> str:
        if count:
            return f"{SELECT} {COUNT_ALL} {FROM} {from_table}"
        else:
            if fields is None:
                return f"{SELECT} {ALL} {FROM} {from_table}"
            else:
                return f"{SELECT} {', '.join(fields)} {FROM} {from_table}"

    def select(self, from_table: str, fields: list = None, count: bool = False, random_record: bool = False) -> None:
        if count:
            self._statements.append(self._select(count=True, from_table=from_table))
        else:
            self._statements.append(self._select(fields=fields, from_table=from_table))
        if random_record:
            self._statements.append(self.sort(RAND))
            self._statements.append(self.limit(1))

    def union(self, all: bool = False) -> None:
        if all:
            self._statements.append(f"{UNION} ALL")
        else:
            self._statements.append(UNION)

    @staticmethod
    def _where(field, value: object, from_table: str = None, operator: str = "=", year: bool = False, and_clause: bool = False) -> str:
        table_name = f"{from_table}." if from_table is not None else ""
        field.value = value
        clause = AND if and_clause else WHERE
        field_name = f"{table_name}{field.name}" if not year else f"{YEAR}({table_name}{field.name})"
        return f" {clause} {field_name} {operator} {field.formatted_value(operator==LIKE)}"

    def where(self, field, value: object, from_table: str = None, operator: str = "=", year: bool = False) -> None:
        where_clause = self._where(field, value, from_table, operator, year, WHERE in self._statements[-1])
        if ON_DUPLICATE_KEY in self._statements[-1]:
            self._statements[-1] = self._wedge(where_clause, keyword=ON_DUPLICATE_KEY)
        else:
            self._statements[-1] += where_clause

    def limit(self, count: int, offset: int = None) -> None:
        """

        :param count:
        :param offset: record to begin selecting from (e.g., with count=3 and offset=4, query selects records 5-7)
        """
        prefix = "" if offset is None else f"{offset},"
        self._statements.append(f"{LIMIT} {prefix}{count}")

    def sort(self, by: str, desc: bool = True) -> None:
        suffix = f" {DESC}" if desc else ""
        self._statements[-1] += f" {ORDER_BY} {by}{suffix}"

    def group(self, by: str) -> None:
        self._statements.append(f"{GROUP_BY} {by}")

    @staticmethod
    def _join(foreign_table: str, base_table: str, on: str or list, kind: str) -> str:
        fields_to_join_on = [f"{base_table}.{field}={foreign_table}.{field}" for field in on]
        return f" {JOIN_TYPES.get(kind)} {foreign_table} {ON} {', '.join(fields_to_join_on)}"

    def join(self, foreign_table: str, base_table: str, on: str or list, kind: str = 'inner') -> None:
        join_statement = self._join(foreign_table, base_table, on if isinstance(on, list) else [on], kind)
        if f"{ON_DUPLICATE_KEY}" in self._statements[-1]:
            self._statements[-1] = self._wedge(join_statement, keyword=ON_DUPLICATE_KEY)
        elif f"{UPDATE}" in self._statements[-1]:
            self._statements[-1] = self._wedge(join_statement, keyword=SET)
        else:
            self._statements[-1] += join_statement

    def set_safe_updates(self, command: int) -> None:
        self._statements.append(f"{SET} {SQL_SAFE_UPDATES}={command}")

    def _wedge(self, wedge_statement: str, keyword: str) -> str:
        split_upsert = self._statements[-1].split(f"{keyword} ")
        insert_statement = split_upsert[0]
        update_statement = split_upsert[1]
        return insert_statement + wedge_statement + f" {keyword} " + update_statement

    @property
    def value(self) -> str:
        return self.__repr__()

    @property
    def select_statements(self) -> str:
        return " ".join(self._statements)

    @property
    def statements(self) -> list:
        return self._statements

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return ";".join(self._statements)
