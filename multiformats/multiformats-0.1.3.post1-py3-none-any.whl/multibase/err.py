"""
    Errors for the :mod:`~multiformats.multibase` module.
"""

import builtins

class MultibaseKeyError(builtins.KeyError): # pylint: disable = redefined-builtin
    """ Class for :mod:`~multiformats.multibase` key errors. """
    ...

class MultibaseValueError(builtins.ValueError): # pylint: disable = redefined-builtin
    """ Class :mod:`~multiformats.multibase` value errors. """
    ...
