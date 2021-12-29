# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bmptoduet']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.4.0,<9.0.0', 'numpy>=1.21.5,<2.0.0']

entry_points = \
{'console_scripts': ['bmptoduet = bmptoduet.bmptoduet:cli']}

setup_kwargs = {
    'name': 'bmptoduet',
    'version': '0.1.1',
    'description': 'Convert Monochrome BMP to Duet3D Menu Image',
    'long_description': '# bmptoduet\nConvert Monochrome BMP to Duet3D Menu Image\n\nFor the Duet 12864 menu system - https://duet3d.dozuki.com/Wiki/Duet_2_Maestro_12864_display_menu_system',
    'author': 'Kieran David Evans',
    'author_email': 'keyz182@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/keyz182/bmptoduet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
