# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyxel_lander']

package_data = \
{'': ['*'], 'pyxel_lander': ['assets/*']}

install_requires = \
['pyxel>=1.5.5,<2.0.0']

entry_points = \
{'console_scripts': ['pyxel-lander = pyxel_lander:Game']}

setup_kwargs = {
    'name': 'pyxel-lander',
    'version': '1.4.0',
    'description': 'Lunar Lander game tribute written in Python with Pyxel retro game engine',
    'long_description': '# Pyxel Lander\n\n[![PyPI](https://img.shields.io/pypi/v/pyxel-lander.svg)](https://pypi.org/project/pyxel-lander/)\n[![PyPI - License](https://img.shields.io/pypi/l/pyxel-lander.svg)](https://pypi.org/project/pyxel-lander/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyxel-lander.svg)](https://pypi.org/project/pyxel-lander/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\nLunar Lander game tribute written in Python with [Pyxel](https://github.com/kitao/pyxel) retro game engine.\n\n![screenshot](https://raw.githubusercontent.com/humrochagf/pyxel-lander/master/images/screenshot.png)\n\n## Features\n\n- Procedural map generation\n- Pixel perfect collision detection\n- Fuel propulsion system\n- HUD with the Lunar Module feedback\n- Landing impact detection\n\n## Controls\n\n- Use the `arrow` keys to control the Lunar Module.\n- The `s` key starts the game.\n- You can change maps with the `m` key on the menu.\n- The `r` key restarts the game.\n- You can exit the game with the `q` or `esc` keys.\n\n## Packaged executable\n\nIf you want to play the game without installing the development tools you can check it on [itch.io](https://humrochagf.itch.io/pyxel-lander).\n\n## PyPI Installation\n\nThis game runs with Python 3.7 or above.\n\nYou can use [pipx](https://pipxproject.github.io/pipx/) to install the game and have it available as an standalone program:\n\n```shell\npipx install pyxel-lander\n```\n\nThen you can run the game running:\n\n```shell\npyxel-lander\n```\n\n**Warning:** The Pyxel requirement uses external libraries, make sure you have them all installed by looking into its [docs](https://github.com/kitao/pyxel#how-to-install).\n\n## Running from source code\n\nTo run it from the source code you need first to clone from the repository:\n\n```shell\ngit clone https://github.com/humrochagf/pyxel-lander.git\n```\n\nAfter cloned, access the folder and install its dependencies with [poetry](https://python-poetry.org/):\n\n```shell\ncd pyxel-lander/\npoetry install\n```\n\nWith everything installed run the game with:\n\n```shell\npoetry run python -m pyxel_lander\n```\n',
    'author': 'Humberto Rocha',
    'author_email': 'humrochagf@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/humrochagf/pyxel-lander',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
