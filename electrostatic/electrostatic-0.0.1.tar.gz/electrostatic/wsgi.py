"""WSGI interface

The WSGI interfaces for electrostatic.
"""


class Electrostatic:
    def __init__(self) -> None:
        pass

    def __call__(self, environ, start_response) -> None:
        raise NotImplementedError("Not implemented yet, sorry!")
