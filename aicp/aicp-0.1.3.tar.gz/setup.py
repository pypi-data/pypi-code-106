# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aicp']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['aicp = aicp.main:app']}

setup_kwargs = {
    'name': 'aicp',
    'version': '0.1.3',
    'description': '',
    'long_description': '# AI Collaboration Platform\n\n## Install\n\n    pip install aicp\n\n\n## Prerequisites\n\n    * Python 3.6+\n\n\n## Usage\n\nLogin to the platform using the following command:\n\n    aicp login\n\n\nCreate service with <directory> as the directory using the following command:\n\n    aicp service create <directory>\n\n\nor import service from a local directory using the following command:\n\n    aicp service import <directory> ',
    'author': 'Tobias Oberrauch',
    'author_email': 'tobias.oberrauch@pioneers.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
