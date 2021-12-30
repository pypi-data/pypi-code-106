# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gns3_client']

package_data = \
{'': ['*']}

install_requires = \
['logzero>=1.7.0,<2.0.0',
 'requests-cache>=0.8.1,<0.9.0',
 'requests>=2.26.0,<3.0.0',
 'urllib3>=1.26.7,<2.0.0']

setup_kwargs = {
    'name': 'gns3-client',
    'version': '0.1.0',
    'description': 'Python API client for GNS3 network simulation tool',
    'long_description': "[![Python 3.9](https://img.shields.io/badge/python-3.9-green.svg)](https://docs.python.org/3.9/)\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\n# gns3-client\n\n*gns3-client* is a Python library that can be used to interact with a [GNS3 server](https://github.com/GNS3/gns3-server)\nusing its HTTP REST API. A GNS3 server manages emulators or hypervisors such as Dynamips, VirtualBox or Qemu/KVM.\n\n## Disclaimer\n\nThis library does not aim at explaining nor documenting in any way the GNS3 server API. Please check\nthe [GNS3 server official documentation](https://gns3-server.readthedocs.io/en/latest/index.html) for further\ninformation.\n\n## Getting Started\n\nTests provide a very good starting point.\n\n### Prerequisites\n\nYou'll need a [GNS3 server](https://github.com/GNS3/gns3-server) appliance or virtual machine to use the library.\nInstructions on how to install a server appliance or virtual machine can be found on\nthe [GNS3 website](https://www.gns3.com/).\n\n### Installing\n\n```\npip install gns3-client\n```\n\n## Running the tests\n\nYou'll need a [GNS3 server](https://github.com/GNS3/gns3-server) appliance or virtual machine to test the library.\nInstructions on how to install a server appliance or virtual machine can be found on\nthe [GNS3 website](https://www.gns3.com/).\n\nLocation of this test server is provided via these 2 environment variables:\n\n| Environment variable name | Description                                 |             Example             |\n|:-------------------------:|---------------------------------------------|:-------------------------------:|\n|     `GNS3_SERVER_URL`     | The URL of the GNS3 test server             | http://gns3.example.com:3080/v2 |\n\nYou then simply need to perform a `python -v tests/`.\n\n## Limitations\n\nIn this version, all [CRUD operations](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) of the following\nobject types have been implemented:\n\n- projects\n- templates\n- nodes\n- links\n- drawings\n\n## Contributing\n\nPlease read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.\n\n## Building\n\n```\npoetry build\npoetry publish\n```\n\n## Versioning\n\nWe use [SemVer](http://semver.org/) for versioning. For the versions available, see\nthe [tags on this repository](https://github.com/desnoe/gns3-client/tags).\n\n## Authors\n\n* **Olivier Desnoë** - *Initial work* - [Albatross Networks](http://albatross-networks.com)\n\nSee also the list of [contributors](https://github.com/desnoe/gns3-client/contributors) who participated in this\nproject.\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\n",
    'author': 'Olivier Desnoe',
    'author_email': 'olivier@delarche.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/desnoe/gns3-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
