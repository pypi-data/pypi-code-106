import os


def getenv(key,
           default='',
           wrapper=str):
    """
    Returns casted environment value of key with default replace in case of None
    """

    return wrapper(os.getenv(key, default))
