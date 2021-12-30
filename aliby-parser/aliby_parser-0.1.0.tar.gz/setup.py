# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aliby_parser']

package_data = \
{'': ['*'], 'aliby_parser': ['grammars/*']}

setup_kwargs = {
    'name': 'aliby-parser',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alan Munoz',
    'author_email': 'alan.munoz@ed.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
