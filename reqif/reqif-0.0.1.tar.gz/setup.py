# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reqif',
 'reqif.cli',
 'reqif.commands',
 'reqif.commands.dump',
 'reqif.commands.format',
 'reqif.commands.passthrough',
 'reqif.commands.validate',
 'reqif.helpers',
 'reqif.models',
 'reqif.parsers',
 'reqif.parsers.spec_types']

package_data = \
{'': ['*'], 'reqif.commands.dump': ['templates/*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0', 'jinja2>=2.11.2,<3.0.0', 'lxml>=4.6.2,<5.0.0']

entry_points = \
{'console_scripts': ['reqif = reqif.cli.main:main']}

setup_kwargs = {
    'name': 'reqif',
    'version': '0.0.1',
    'description': 'Python library for ReqIF format. ReqIF parsing and unparsing.',
    'long_description': '# ReqIF\n\nReqIF is a Python library for working ReqIF format.\n\n**The project is under construction.**\n\n## Getting started\n\nTBD\n\n## Usage\n\n### Passthrough command\n\nTBD\n\n### HTML dump\n\nTBD\n\n### Formatting ReqIF\n\nTBD\n\n## Implementation details\n\n### Tolerance\n\nThe first-stage parser is made tolerant against possible issues in ReqIF.\nIt should be possible to parse a ReqIF file even if it is missing important\ninformation. A separate validation command shall be used to confirm the validity\nof the ReqIF contents.\n\n## A bottom-up overview of the ReqIF format\n\n- ReqIF is a standard. See reference document [RD01](#rd01-reqif-standard).\n- ReqIF has a fixed structure (see "What is common for all ReqIF documents" \nbelow)\n- ReqIF standard does not define a document structure for every documents so\na ReqIF tool implementor is free to choose between several implementation \napproaches. There is a\n[ReqIF Implementation Guide](#rd02-reqif-implementation-guide)\nthat attempts to harmonize ReqIF tool developments. See also\n"What is left open by the ReqIF standard" below.\n- ReqIF files produced by various tool often have incomplete schemas. \n\n### What is common for all ReqIF documents\n\n- All documents have ReqIF tags:\n  - Document metadata is stored inside tags of `REQ-IF-HEADER` tag.\n  - Requirements are stored as `<SPEC-OBJECT>`s\n  - Requirements types are stored as `<SPEC-TYPE>`s\n  - Supported data types are stored as `<DATATYPE>`\n  - Relationships such as \'Parent-Child\' as stored as `<SPEC-RELATIONS>`\n\n### What is left open by the ReqIF standard\n \n- How to distinguish requirements from headers/sections?\n  - One way: create separate `SPEC-TYPES`: one or more for requirements and\n    one for sections.\n  - Another way: have one spec type but have it provide a `TYPE` field that can\n  be used to distinguish between `REQUIREMENT` or `SECTION`.\n\n## Reference documents\n\n### [RD01] ReqIF standard\n\nThe latest version is 1.2:\n[Requirements Interchange Format](https://www.omg.org/spec/ReqIF)\n\n### [RD02] ReqIF Implementation Guide \n\n[ReqIF Implementation Guide](https://www.prostep.org/fileadmin/downloads/PSI_ImplementationGuide_ReqIF_V1-7.pdf)\n',
    'author': 'Stanislav Pankevich',
    'author_email': 's.pankevich@gmail.com',
    'maintainer': 'Stanislav Pankevich',
    'maintainer_email': 's.pankevich@gmail.com',
    'url': 'https://github.com/strictdoc-project/reqif',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
