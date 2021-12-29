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
    'version': '1.0.0',
    'description': 'bolb',
    'long_description': '# bolb\n\n```py\nfrom bolb import bolb\n\nprint(bolb())\n```\n',
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vcokltfre/bolb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
