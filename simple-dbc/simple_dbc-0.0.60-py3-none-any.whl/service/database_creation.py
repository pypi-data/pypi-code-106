from typing import List, Tuple

import pandas as pd
from pandaSuit.df import DF

from dbc.connect import DatabaseClient
from dbc.service.lite.table import Table
from dbc.service.lite.field import Field
from dbc.query.query import Query
from dbc.domain.reference import Reference
from dbc.domain.table import Table as DataBaseTable
from dbc.domain.fields.field import DatabaseFieldType
# from dbc.domain.fields.text import Text
from dbc.common.constants.field import *
from dbc.common.constants.misc import YES
from dbc.common.constants import query as query_constants
from dbc.common.constants import query_headers


def create_tables(tables: List[DataBaseTable], db_credentials: dict) -> None:
    lite_tables = _create_lite_tables(tables)
    db_client = DatabaseClient(db_credentials)
    existing_tables = _get_existing_tables(db_client)
    ordered_tables = _order_tables_for_creation(lite_tables, [])
    must_create, alter_table_queries = _categorize_tables(ordered_tables, existing_tables)
    if len(must_create) > 0:
        create_tables_query = Query()
        create_tables_query.create_tables(must_create)
        db_client.write(create_tables_query)
    if len(alter_table_queries) > 0:
        db_client.write(alter_table_queries)


def _categorize_tables(ordered_tables: List[Table], existing_tables: List[Table]) -> tuple:
    must_create, must_alter = [], []
    for table in ordered_tables:
        if table not in existing_tables:
            if table.name.lower() in [existing_table.name for existing_table in existing_tables]:
                must_alter.append(table)
            else:
                must_create.append(table)
    return must_create, _create_modify_table_queries(must_alter, {table.name: table for table in existing_tables})


def _create_modify_table_queries(tables_to_alter: List[Table], existing_table_mapping: dict) -> list:
    modify_queries = []
    for table in tables_to_alter:
        modify_queries += table.difference(existing_table_mapping.get(table.name.lower()))
    return modify_queries


def _create_lite_tables(tables: List[DataBaseTable]) -> List[Table]:
    table_defs = []
    for table in tables:
        table_instance = table()
        _table = {"name": table_instance.name, "table_fields": [_create_lite_field(field) for field in table_instance.fields]}
        try:
            _table["unique_index"] = table_instance.unique_index
        except AttributeError:
            pass
        finally:
            table_defs.append(Table(**_table))
    return table_defs


def _create_lite_field(field: DatabaseFieldType) -> Field:
    return Field(**{
        "type": _get_type(field.type),
        "name": field.name,
        "value": None,
        "pk": field.pk,
        "fk": field.fk,
        "references": {"table_name": field.references.table_name, "field_name": field.references.field_name} if field.fk else None,
        "characters": field.characters,
        "nullable": field.nullable,
        "unique": True if field.pk else field.unique,
        "index": True if field.pk else field.index,
        "options": field.options,
        "signed": field.signed,
        "float_size": field.float_size,
        "decimal_size": field.decimal_size,
        "extra": field.extra,
        "default": field.default
    })


def _order_tables_for_creation(tables: List[Table], ordered_tables: List[Table]) -> list:
    if len(tables) > 0:
        table = tables.pop(0)
        if not table.has_foreign_keys:
            ordered_tables.append(table)
        else:
            if _all_related_tables_already_added(ordered_tables, table.related_to):
                ordered_tables.append(table)
            else:
                tables.append(table)
        return _order_tables_for_creation(tables, ordered_tables)
    else:
        return ordered_tables


def _all_related_tables_already_added(ordered_tables: List[Table], related_table_names: list) -> bool:
    def already_added(table_name: str) -> bool:
        return table_name in [table.name for table in ordered_tables]
    return all(already_added(related_table_name) for related_table_name in related_table_names)


def _get_existing_tables(db_client: DatabaseClient) -> List[Table]:
    show_tables_query = Query()
    show_tables_query.show_tables()
    current_db_tables = [table[0] for table in db_client.read(show_tables_query)]
    table_descriptions = []
    for current_db_table in current_db_tables:
        describe_query = Query()
        describe_query.describe_table(current_db_table)
        table_descriptions.append(_parse_table_description(
            current_db_table, DF(data=pd.DataFrame(data=db_client.read(describe_query), columns=query_headers.DESCRIBE)), db_client
        ))
    return table_descriptions


def _parse_table_description(table_name: str, table_description: DF, db_client: DatabaseClient) -> Table:
    unique_index = _get_unique_index_if_one_exists(table_name, db_client)
    return Table(**{
        'name': table_name,
        'table_fields': [_parse_field_description(table_name, field_description, db_client)
                         for field_description in table_description.rows],
        'unique_index': unique_index
    })


def _parse_field_description(table_name: str, field_description: pd.Series, db_client: DatabaseClient) -> Field:
    field_name = field_description.to_dict().get("Field")
    type_name = _get_type(str(field_description.to_dict().get("Type")))
    pk = field_description.to_dict().get("Key") == PRIMARY
    fk = field_description.to_dict().get("Key") == FOREIGN
    if fk:
        reference_found = _get_reference(table_name, field_name, db_client)
        if reference_found is not None:
            reference, fk_constraint_name = reference_found
        else:
            fk, reference, fk_constraint_name = False, None, None
    else:
        reference, fk_constraint_name = None, None
    field_data = {
        'type': type_name,
        'name': field_name,
        'value': None,
        'pk': pk,
        'fk': fk,
        "_fk_constraint_name": fk_constraint_name,
        'references': reference,
        'characters': _get_characters(type_name, str(field_description.to_dict().get("Type"))),
        'nullable': field_description.to_dict().get("Null") == YES,
        'unique': _get_unique(field_description.to_dict().get("Key")),
        'index': pk,
        'options': _get_options(type_name, str(field_description.to_dict().get("Type"))),
        'signed': _get_signed(type_name, str(field_description.to_dict().get("Type"))),
        'float_size': _get_float_size(type_name, str(field_description.to_dict().get("Type"))),
        'decimal_size': _get_decimal_size(type_name, str(field_description.to_dict().get("Type"))),
        'extra': _get_extra(field_description.to_dict().get("Extra")),
        'default': field_description.to_dict().get("Default")
    }
    return Field(**field_data)


def _get_type(value: str) -> str:
    if "(" in value:
        temp_type = value.split("(")[0]
        if "'" in temp_type:
            type_name = temp_type.split("'")[1]
        elif '"' in temp_type:
            type_name = temp_type.split('"')[1]
        else:
            type_name = temp_type
    else:
        type_name = value
    if type_name in ["smallint", "mediumint", "tinyint", "bigint"]:  # todo: ensure that bigint is the correct type
        if "tinyint(1)" in value:
            return BOOL
        else:
            return type_name
    elif type_name == DECIMAL:
        return FLOAT
    elif (DATE in type_name and type_name != DATE) or (TEXT in type_name and type_name != TEXT):
        return type_name.split("'")[1].split("\\")[0]
    else:
        return type_name


def _get_unique(value: str) -> bool:
    if value == UNIQUE or value == PRIMARY:
        return True
    else:
        return False


def _get_characters(type_name: str, field_type: str) -> int or None:
    if type_name == VARCHAR:
        return int(field_type.split("(")[1].split(")")[0])
    else:
        return None


def _get_options(type_name: str, field_type: str) -> set or None:
    if type_name == ENUM:
        return set(field_type.split("enum(")[1].split(')"')[0][1:-1].split("','"))
    else:
        return None


# def _get_index(table_name: str, field_name: str, reference: Field, db_client: DatabaseClient) -> bool:
#     if reference is not None:  # then this is a foreign key, and therefore already indexed
#         return False
#     else:  # then this is not a foreign key, and may be an index (where the index name IS the field name)
#         query = Query()
#         query.show_index(table_name)
#         query.where(Text(name=query_constants.COLUMN_NAME), value=field_name)
#         indexes = DF(data=pd.DataFrame(data=db_client.read(query), columns=query_headers.SHOW_INDEX))
#         if indexes.row_count == 0:
#             return False
#         if indexes.row_count == 1:
#             return indexes.select(column=query_constants.KEY_NAME) == indexes.select(column=query_constants.COLUMN_NAME)
#         else:
#             return indexes.where(column_name=query_constants.KEY_NAME, some_value=query_constants.COLUMN_NAME,
#                                  pandas_return_type=False).row_count > 0


def _get_extra(extra: str) -> str or None:
    return extra if len(extra) > 0 else None


def _get_signed(type_name: str, field_type: str) -> bool:
    if type_name == INT:
        return SIGNED in field_type.split()
    elif type_name == FLOAT:
        return True
    else:
        return False


def _get_float_size(type_name: str, field_type: str) -> int or None:
    if type_name == FLOAT:
        return int(field_type.split("decimal(")[1].split(",")[0])
    else:
        return None


def _get_decimal_size(type_name: str, field_type: str) -> int or None:
    if type_name == FLOAT:
        return int(field_type.split("decimal(")[1].split(",")[1].split(")")[0])
    else:
        return None


def _get_reference(table_name: str, field_name: str, db_client: DatabaseClient) -> Tuple[Reference, str]:
    def _extract_reference_table_and_field(foreign_field: str) -> Tuple[Reference, str]:
        foreign_table_name = foreign_field.split("REFERENCES `")[1].split("`")[0]
        foreign_field_name = foreign_field.split("REFERENCES `")[1].split("(`")[1].split("`)")[0]
        describe_query = Query()
        describe_query.describe_table(foreign_table_name)
        fields = DF(data=pd.DataFrame(data=db_client.read(describe_query), columns=query_headers.DESCRIBE))
        for field_info in fields.rows:
            if field_info.select("Field") == foreign_field_name:
                constraint_name = foreign_field.split("`")[1].split("`")[0]
                return Reference(table_name=foreign_table_name, field_name=foreign_field_name), constraint_name

    query = Query()
    query.show_create_table(table_name)
    create_table_statement = db_client.read(query)[0][1]
    for field in create_table_statement.split(CONSTRAINT)[1:]:
        if field.split("(`")[1].split("`)")[0] == field_name:
            return _extract_reference_table_and_field(field)


def _get_unique_index_if_one_exists(table_name: str, db_client: DatabaseClient) -> dict or None:
    query = Query()
    query.show_create_table(table_name)
    create_table_statement = db_client.read(query)[0][1]
    for unique_key in create_table_statement.split(query_constants.UNIQUE_KEY)[1:]:
        fields = list(unique_key.split("(")[1].split(")")[0].replace("`", "").split(","))
        if len(fields) > 1:
            return {
                "name": unique_key.split("`")[1],
                "field_names": fields
            }
    return None
