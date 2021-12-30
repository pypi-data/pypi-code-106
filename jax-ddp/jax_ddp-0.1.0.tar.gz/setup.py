# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jax_ddp', 'jax_ddp.plants', 'jax_ddp.solvers']

package_data = \
{'': ['*']}

install_requires = \
['jax', 'jaxlib', 'plotly>=5.1.0,<6.0.0', 'tqdm']

setup_kwargs = {
    'name': 'jax-ddp',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'David Browne',
    'author_email': 'davidbrowne@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.12,<3.10',
}


setup(**setup_kwargs)
