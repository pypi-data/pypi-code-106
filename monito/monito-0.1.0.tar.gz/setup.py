# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monito']

package_data = \
{'': ['*']}

install_requires = \
['alive-progress>=2.1.0,<3.0.0',
 'bs4>=0.0.1,<0.0.2',
 'feedparser>=6.0.8,<7.0.0',
 'lxml>=4.7.1,<5.0.0',
 'requests>=2.26.0,<3.0.0',
 'selenium>=4.1.0,<5.0.0',
 'spacy-syllables>=3.0.1,<4.0.0',
 'spacy>=3.2.1,<4.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['lic = monito.monito_main:run']}

setup_kwargs = {
    'name': 'monito',
    'version': '0.1.0',
    'description': 'Tool to monitor and filter news websites and alike.',
    'long_description': "monito\n======\n\nTool for monitoring and filtering news websites and alike.\n\nInstallation\n============\n\nThe installation is straight forward. You can install the package via ``pip``, ``pipenv``, ``poetry``\nand alike or by downloading the source from the gitlab repository.\n\nFrom pypi.org (recommended)\n---------------------------\n\nInstall by typing\n\n.. code-block:: shell\n\n                pip install monito\n\nor\n\n.. code-block:: shell\n\n                pip install --user monito\n\nif you do not have root access.\n\nPlease check the documentations for `pipenv <https://pipenv.pypa.io/en/latest/>`_, and\n`poetry <https://python-poetry.org/docs/>`_ for information on how to install packages with these tools.\n\n\nFrom gitlab.com\n---------------\n\nTo get the latest features or contribute to the development, you can clone the whole project using\n`git <https://git-scm.com/>`_:\n\n.. code-block:: shell\n\n                git clone https://gitlab.com/szs/monito.git\n\nNow you can, for instance, copy ``monito.py`` over to your project and import it directly or use it as a\ncommand line tool.\n\n\nHow to Contribute\n=================\n\nIf you find a bug, want to propose a feature or need help getting this package to work with your data\non your system, please don't hesitate to file an `issue <https://gitlab.com/szs/monito/-/issues>`_ or write\nan email. Merge requests are also much appreciated!\n\nProject links\n=============\n\n* `Repository <https://gitlab.com/szs/monito>`_\n* `Documentation <https://monito.readthedocs.io/en/latest/>`_\n* `pypi page <https://pypi.org/project/monito/>`_\n\nAuthor\n======\n\nSteffen Brinkmann <s-b@mailbox.org>\n\nLicense\n=======\n\nPublished under the terms of the `MIT license <https://mit-license.org/>`_\n",
    'author': 'Steffen Brinkmann',
    'author_email': 's-b@mailbox.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/szs/monito/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
