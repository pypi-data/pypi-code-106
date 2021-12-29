# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wagtail_localize_panel', 'wagtail_localize_panel.migrations']

package_data = \
{'': ['*'],
 'wagtail_localize_panel': ['templates/wagtail_localize_panel/home/*']}

install_requires = \
['Django>=3.2.4,<4.0.0', 'wagtail-localize>=1.0,<2.0', 'wagtail>=2.14.1,<3.0.0']

setup_kwargs = {
    'name': 'wagtail-localize-panel',
    'version': '0.2.1',
    'description': 'Wagtail localize panel and notification',
    'long_description': "Wagtail Localize Panel\n======================\n\n.. image:: https://readthedocs.org/projects/wagtail-localize-panel/badge/?version=latest\n   :target: https://wagtail-localize-panel.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n\n\nA Wagtail plugin to help content writer and translator to keep translation\nup to date.\n\n.. image:: https://raw.githubusercontent.com/Gandi/wagtail-localize-panel/main/screenshot.png\n   :alt: Translation panel example\n\n\nSettings\n--------\n\nLOCALIZE_PANEL_APP_NAME = 'my_app_name'\n",
    'author': 'Guillaume Gauvrit',
    'author_email': 'guillaume@gandi.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Gandi/wagtail-localize-panel',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
