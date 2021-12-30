# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sei_client']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'sei-client',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'Julio Cezar Riffel',
    'author_email': 'julioriffel@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
