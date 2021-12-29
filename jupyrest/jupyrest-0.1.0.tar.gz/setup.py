# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jupyrest', 'jupyrest.workers', 'jupyrest.workers.generated']

package_data = \
{'': ['*']}

install_requires = \
['azure-storage-blob>=12.8.1,<13.0.0',
 'black==21.7b0',
 'click>=7.1.2,<8.0.0',
 'cryptography<=3.4.7',
 'entrypoints>=0.3,<0.4',
 'fastapi>=0.65.2,<0.66.0',
 'grpcio-tools>=1.38.0,<2.0.0',
 'grpcio>=1.38.0,<2.0.0',
 'ipykernel>=6.0.1,<7.0.0',
 'ipython>=7.25.0,<8.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'jupyter-client<=6.1.12',
 'nbclient>=0.5.1,<0.6.0',
 'nbconvert==5.6.1',
 'nbformat>=5.1.3,<6.0.0',
 'opentelemetry-api>=1.5.0,<2.0.0',
 'papermill>=2.2,<2.3',
 'pydantic>=1.8,<2.0',
 'scrapbook>=0.5.0,<0.6.0',
 'setuptools-rust>=0.12.1,<0.13.0',
 'textwrap3>=0.9.2,<0.10.0',
 'typer>=0.3.2,<0.4.0',
 'uvicorn>=0.14.0,<0.15.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=3.7.4,<4.0.0'],
 ':sys_platform == "win32"': ['pywin32==301']}

setup_kwargs = {
    'name': 'jupyrest',
    'version': '0.1.0',
    'description': 'A tool to expose Jupyter notebooks as a REST API.',
    'long_description': None,
    'author': 'Koushik Krishnan',
    'author_email': 'kokrishn@microsoft.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.9',
}


setup(**setup_kwargs)
