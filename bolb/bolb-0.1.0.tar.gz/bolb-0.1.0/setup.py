# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bolb']

package_data = \
{'': ['*']}

install_requires = \
['taskipy>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'bolb',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
