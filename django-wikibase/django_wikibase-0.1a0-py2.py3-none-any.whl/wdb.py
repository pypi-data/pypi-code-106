from urllib.request import urlopen
from json import loads
from typing import List

charset_map = dict()

# https://github.com/yuvipanda/python-wdqs/blob/master/wdqs/client.py


class WbDatabase:
    SHRT_MIN = 1
    SHRT_MAX = 1
    INT_MIN = 1
    INT_MAX = 1
    LONG_MIN = 1
    LONG_MAX = 1

    ISOLATION_LEVEL_READ_COMMITED = 1

    _MEDIAWIKI_VERSION = '_mediawiki_version'
    _INSTANCE_OF = 'instance of'
    _SUBCLASS_OF = 'subclass of'
    _DJANGO_MODEL = 'django model'
    _SPARQL_ENDPOINT = '_sparql_endpoint'

    class Error:
        ...

    class DatabaseError(BaseException):
        ...

    class IntegrityError(BaseException):
        ...

    class OperationalError(BaseException):
        ...

    class DataError(BaseException):
        ...

    class InternalError(BaseException):
        ...

    class NotSupportedError(BaseException):
        ...

    class InterfaceError(BaseException):
        ...

    class ProgrammingError(BaseException):
        ...

    @staticmethod
    def connect(charset: str = 'utf8', url: str = '',
                user: str = '', password: str = '',
                instance_of_property_id: int = None,
                subclass_of_property_id: int = None,
                django_model_item_id: int = None,
                wdqs_sparql_endpoint: str = None):
        return WbDatabaseConnection(charset, url,
                                    user, password,
                                    instance_of_property_id,
                                    subclass_of_property_id,
                                    django_model_item_id,
                                    wdqs_sparql_endpoint)


class WbCursor:

    def close(self):
        print('close')

    def execute(self, query, params):
        print(f'execute ${query} with ${params}')

    def fetchall(self):
        """Fetch rows from the wikibase

        Returns:
            List[Tuple]: List of rows from the wikibase
        """
        return iter(())

    def fetchone(self):
        """Fetch single row from the wikibase

        Returns:
            Tuple: the row from the wikibase
        """
        return ()


class WbDatabaseConnection:

    def __init__(self, charset: str, url: str,
                 user: str, password: str,
                 instance_of_property_id: int,
                 subclass_of_property_id: int,
                 django_model_item_id: int,
                 wdqs_sparql_endpoint: str):
        self.charset = charset
        self.url = url
        self.user = user
        self.password = password  # TODO: hash instead plain
        # TODO: if django_model_item_id not defined create item in the wikibase.
        if not django_model_item_id:
            django_model_item_id = 49
        mediawiki_info = loads(urlopen(
            f'{url}/api.php?action=query&meta=siteinfo&format=json').read().decode(charset))
        wikibase_conceptbaseuri = mediawiki_info['query']['general']['wikibase-conceptbaseuri']
        # https://avangard.testo.click/api.php?action=query&meta=siteinfo&siprop=extensions&format=json
        self.wikibase_info = {
            WbDatabase._MEDIAWIKI_VERSION: mediawiki_info['query']['general']['generator'],
            WbDatabase._INSTANCE_OF: f'{wikibase_conceptbaseuri}P{instance_of_property_id}',
            WbDatabase._SUBCLASS_OF: f'{wikibase_conceptbaseuri}P{subclass_of_property_id}',
            WbDatabase._DJANGO_MODEL: f'{wikibase_conceptbaseuri}Q{django_model_item_id}',
            WbDatabase._SPARQL_ENDPOINT: wdqs_sparql_endpoint if wdqs_sparql_endpoint else f'{url}/sparql'
        }
        self.transactions = []

    def db_info(self, key):
        return self.wikibase_info.get(key)

    def cursor(self):
        return WbCursor()

    def rollback(self):
        ...

    def commit(self):
        ...

    def close(self):
        ...

    def trans(self) -> List:
        return self


class TransactionContext:

    def __init__(self, connection: WbDatabaseConnection):
        self.connection = connection

    def __enter__(self):
        # make a database connection and return it
        ...
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.connection.close()
        ...
