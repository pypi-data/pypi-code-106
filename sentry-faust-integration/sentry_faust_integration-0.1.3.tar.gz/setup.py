# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sentry_faust_integration']

package_data = \
{'': ['*']}

install_requires = \
['faust>=1.10.4,<2.0.0', 'sentry-sdk>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'sentry-faust-integration',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'dmitry',
    'author_email': 'dmitrysmirnov931@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
