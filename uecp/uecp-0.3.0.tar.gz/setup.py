# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uecp', 'uecp.commands', 'uecp.serial_con']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.2.0,<22.0.0',
 'crc>=1.1.2,<2.0.0',
 'pyserial-asyncio>=0.6,<0.7',
 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'uecp',
    'version': '0.3.0',
    'description': 'UECP encoder & decoder',
    'long_description': '# python UECP implementation\n\nThis library aims to support UECP version 6.02. It will start with basic commands required to support our needs.\n',
    'author': 'Christian Kohlstedde',
    'author_email': 'christian@kohlsted.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
