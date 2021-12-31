# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nlx', 'nlx.conf', 'nlx.utils']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'requests>=2.26.0,<3.0.0',
 'rich>=10.16.1,<11.0.0']

entry_points = \
{'console_scripts': ['nlx = nlx.main:main']}

setup_kwargs = {
    'name': 'nlx-cli',
    'version': '0.1.0',
    'description': 'Python SDK for interacting with the NLx API and other affiliated tools',
    'long_description': None,
    'author': 'jjorissen52',
    'author_email': 'jjorissen52@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
