# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['electrostatic', 'tests']

package_data = \
{'': ['*'], 'tests': ['sample/static1/*']}

install_requires = \
['asgiref>=3.4.1,<4.0.0']

extras_require = \
{'watchdog': ['watchdog>=2.1.6,<3.0.0']}

setup_kwargs = {
    'name': 'electrostatic',
    'version': '0.0.1',
    'description': 'Application or middleware to serve static files over ASGI or WSGI',
    'long_description': '# ASGI Static Files\n\n\n[![pypi](https://img.shields.io/pypi/v/electrostatic.svg)](https://pypi.org/project/electrostatic/)\n[![python](https://img.shields.io/pypi/pyversions/electrostatic.svg)](https://pypi.org/project/electrostatic/)\n[![Build Status](https://github.com/LucidDan/electrostatic/actions/workflows/dev.yml/badge.svg)](https://github.com/LucidDan/electrostatic/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/LucidDan/electrostatic/branch/main/graphs/badge.svg)](https://codecov.io/github/LucidDan/electrostatic)\n\n\n\nAn ASGI application or middleware for serving static files\n\n\n* Documentation: <https://luciddan.github.io/electrostatic>\n* GitHub: <https://github.com/LucidDan/electrostatic>\n* PyPI: <https://pypi.org/project/electrostatic/>\n* Free software: MIT\n\n\n## Features\n\n* TODO\n\n## Credits\n',
    'author': 'Dan Sloan',
    'author_email': 'dan@lucidhorizons.com.au',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/LucidDan/electrostatic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
