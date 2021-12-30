# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drf_static_router', 'drf_static_router.tests']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.0,<5.0', 'djangorestframework>=3.13.1,<4.0.0']

setup_kwargs = {
    'name': 'drf-static-router',
    'version': '0.0.1',
    'description': "A DRF router that doesn't generated dynamicly default routes for create/list/retrieve/... actions.",
    'long_description': None,
    'author': 'Aymeric Derbois',
    'author_email': 'aymeric@kenlodin.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
