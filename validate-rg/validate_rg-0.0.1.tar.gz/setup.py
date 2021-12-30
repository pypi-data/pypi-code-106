# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['validate_rg']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'validate-rg',
    'version': '0.0.1',
    'description': 'Faz a validação de RG (SSP SP) Brasileiro',
    'long_description': "# validate-rg\n\n[![pipy](https://img.shields.io/pypi/v/validate_rg.svg)](https://pypi.python.org/pypi/validate_rg)\n\nValidates Brazilian RG (SSP SP)\n\n## Features\n\n- RG Validation with mask\n- RG Validation without mask\n\n## Modes of use\n\n```python\n#!/usr/bin/python\nimport validate_rg\n\n# Without mask\nvalidate_rg.is_valid('505675092') # True\n\n# With mask\nvalidate_rg.is_valid('50.567.509-2') # True\n```\n\nor\n\n```python\n#!/usr/bin/python\nfrom validate_rg import is_valid\n\n# Without mask\nis_valid('111111111') # False\n\n# With mask\nis_valid('11.111.111-1') # False\n```\n\n# Author\n\n[João Filho](https://joaofilho.dev)\n[Github](https://github.com/drummerzzz)\n\n# Credits\n\nThis package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.\n\n[Cookiecutter](https://github.com/audreyr/cookiecutter)\n\n[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)\n\n[DV calculation](https://www.ngmatematica.com/2014/02/como-determinar-o-digito-verificador-do.html)",
    'author': 'Drummerzzz',
    'author_email': 'devdrummerzzz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/drummerzzz/pypi_validate_rg/README.md',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
