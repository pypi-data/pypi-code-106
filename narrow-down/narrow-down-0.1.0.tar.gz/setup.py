# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['narrow_down']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'narrow-down',
    'version': '0.1.0',
    'description': 'Fast fuzzy text search',
    'long_description': '\n# Narrow Down\n\n\n<div align="center">\n\n[![PyPI - Version](https://img.shields.io/pypi/v/narrow-down.svg)](https://pypi.python.org/pypi/narrow-down)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/narrow-down.svg)](https://pypi.python.org/pypi/narrow-down)\n[![Tests](https://github.com/chr1st1ank/narrow-down/workflows/tests/badge.svg)](https://github.com/chr1st1ank/narrow-down/actions?workflow=tests)\n[![Codecov](https://codecov.io/gh/chr1st1ank/narrow-down/branch/main/graph/badge.svg)](https://codecov.io/gh/chr1st1ank/narrow-down)\n[![Read the Docs](https://readthedocs.org/projects/narrow-down/badge/)](https://narrow-down.readthedocs.io/)\n[![PyPI - License](https://img.shields.io/pypi/l/narrow-down.svg)](https://pypi.python.org/pypi/narrow-down)\n\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)\n\n</div>\n\n\nFast fuzzy text search\n\n\n* GitHub repo: <https://github.com/chr1st1ank/narrow-down.git>\n* Documentation: <https://narrow-down.readthedocs.io>\n* Free software: Apache Software License 2.0\n\n\n## Features\n\n* TODO\n\n## Quickstart\n\nTODO\n\n## Credits\n\nThis package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.\n\n[cookiecutter]: https://github.com/cookiecutter/cookiecutter\n[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage\n',
    'author': 'Christian Krudewig',
    'author_email': 'chr1st1ank@krudewig-online.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chr1st1ank/narrow-down',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
