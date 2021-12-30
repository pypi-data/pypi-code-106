# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zscaler_python_sdk', 'zscaler_python_sdk.lib']

package_data = \
{'': ['*']}

install_requires = \
['black>=21.9b0,<22.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'zscaler-python-sdk',
    'version': '0.2.0',
    'description': 'Unofficial Zscaler API python sdk',
    'long_description': '# zscaler-python-sdk',
    'author': 'yuta519',
    'author_email': 'yuta519.ka23tf@docomo.ne.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
