from setuptools import setup

name = "types-regex"
description = "Typing stubs for regex"
long_description = '''
## Typing stubs for regex

This is a PEP 561 type stub package for the `regex` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `regex`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/regex. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `38a08fcf04fd4693253329bd1a2b63a6204b6c48`.
'''.lstrip()

setup(name=name,
      version="2021.11.10.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['regex-stubs'],
      package_data={'regex-stubs': ['__init__.pyi', '_regex.pyi', '_regex_core.pyi', 'regex.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
