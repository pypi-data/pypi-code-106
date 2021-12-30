from mysql.connector import connect, Error as MySQLError

from dbc.query.query import Query
from dbc.common.constants.connect import *


class DatabaseClient:
    def __init__(self, credentials: dict):
        """
        DatabaseClient establishes a connection and provides methods for executing queries
        :param credentials: database host, user, password and database name (if applicable)
        """
        self._host = credentials.get(HOST)
        self._user = credentials.get(USER)
        self._password = credentials.get(PASSWORD)
        self._database = credentials.get(DATABASE)

    def read(self, query: Query) -> list:
        """
        reads and returns result from query
        :param query: read query
        :return: list of records returned from query
        """
        try:
            with connect(host=self._host, user=self._user, password=self._password, database=self._database) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query.select_statements)
                    result = cursor.fetchall()
            return result
        except MySQLError as e:
            print(e)

    def write(self, query: Query, disable_safe_updates: bool = False) -> None:
        """
        writes a query to the database
        :param disable_safe_updates: flag indicating whether or not to ... todo: remember what this is for
        :param query: write query
        """
        try:
            with connect(host=self._host, user=self._user, password=self._password, database=self._database) as connection:
                with connection.cursor() as cursor:
                    if disable_safe_updates:
                        safe_updates_query = Query()
                        safe_updates_query.set_safe_updates(0)
                        cursor.execute(safe_updates_query.value)
                    try:
                        if isinstance(query, list):
                            [cursor.execute(query_object.value) for query_object in query]
                        else:
                            [cursor.execute(statement) for statement in query.statements]
                        connection.commit()
                    except Exception as e:
                        connection.rollback()
                        raise MySQLError(f"Cannot execute query \"{query}\", rolling back changes.\nError: {e}")
                    if disable_safe_updates:
                        safe_updates_query = Query()
                        safe_updates_query.set_safe_updates(1)
                        cursor.execute(safe_updates_query.value)
        except MySQLError as e:
            print(e)
