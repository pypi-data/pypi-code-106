# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfreetts']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyfreetts',
    'version': '0.1.1',
    'description': 'Convert text to speech with the pretty voices',
    'long_description': '<p align="center"><img src="https://raw.githubusercontent.com/tquangsdh20/pyfreetts/master/.github/logo.svg"></p>\n\n<p align="center"> <img src="https://github.com/tquangsdh20/pyfreetts/actions/workflows/test.yml/badge.svg?style=plastic"> <a href="https://codecov.io/github/tquangsdh20/pyfreetts/commit/5d0da7ae595f845c64742d9d64260d7018453856"><img src="https://codecov.io/gh/tquangsdh20/pyfreetts/branch/master/graphs/badge.svg?branch=master"></a></p>\n\n\n## Features\n\n- Support text to speech with many pretty voices options\n- Support download file mp3 from TTS\n\n## Installation\n**Windows**\n```\npython -m pip install pyfreetts\n```\n**Linux**\n```\npip install pyfreetts\n```\n**macOS**\n```\nsudo pip3 install pyfreetts\n```\n## How does it work?\n\n### Setup Language for Converting\n\nTo setup language and voice using the method `setup_voice(language_code)`, where `language_code` :\n\n- English US : `am`\n- English UK : `br`\n- Portuguese (Brazil): `pt-br`\n- Portuguese (Portugal): `pt`\n- The other languages : `ISO LANGUAGE CODE 639-1`\n\n```python\nfrom pyfreetts import Text2Speech\n\nmodule = Text2Speech()\nmodule.setup_voice("am")\nmodule.convert("how are you?")\nmodule.save_to_file("test.mp3")\nmodule.close()\n```\n\nOutput\n\n```\n>> All voices for your language:\n>>    1. Joey - Male - SAPI5\n>>    2. Justin - Male - SAPI5\n>>    3. Matthew - Male - SAPI5\n>>    4. Salli - Female - SAPI5\n>>    5. Joanna - Female - SAPI5\n>>    6. Ivy - Female - SAPI5\n>> Make your choice: 3\n```\n\n<a href="https://github.com/tquangsdh20/mateco"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>',
    'author': 'Joseph Quang',
    'author_email': 'tquangsdh20@fsob.win',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tquangsdh20/mateco',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
