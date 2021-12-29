# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plotly_calplot']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.4,<2.0.0', 'plotly>=5.4.0,<6.0.0', 'streamlit>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'plotly-calplot',
    'version': '0.1.0',
    'description': 'Calendar Plot made with Plotly',
    'long_description': None,
    'author': 'Bruno Rodrigues Silva',
    'author_email': 'b.rosilva1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
