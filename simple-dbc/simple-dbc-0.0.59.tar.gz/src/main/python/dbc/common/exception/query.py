class QueryError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class QuerySyntaxError(QueryError):
    def __init__(self, msg: str):
        super().__init__(msg)
