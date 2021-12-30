# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ddv', 'ddv.settings']

package_data = \
{'': ['*']}

install_requires = \
['configparser>=5.2.0,<6.0.0']

setup_kwargs = {
    'name': 'ddv-settings',
    'version': '0.1.1',
    'description': 'Module for easily reading and exporting settings from files',
    'long_description': '# DDV Settings\n\nModule for easily reading and exporting settings from files\n\n## Example\n\n**settings.ini**\n```\n[a]\nb = c\nd = e\n\n[f]\ng = h\nj = k\n```\n\nCode that loads settings from `settings.ini` and uses them:\n```\nimport os\nimport sys\nfrom ddv.settings import read, export\n\nread("settings.ini")\nexport(sys.modules[__name__], True, "TEST")\n\nprint("Variable TEST_A_B == c")\nprint(TEST_A_B)\n\nprint("Env Var TEST_F_G == h")\nprint(os.environ.get("TEST_F_G"))\n```\n\n**Output:**\n```\nVariable TEST_A_B == c\nc\nEnv Var TEST_F_G == h\nh\n```',
    'author': 'Davide Vitelaru',
    'author_email': 'davide@vitelaru.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/davidevi/ddv-settings',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
