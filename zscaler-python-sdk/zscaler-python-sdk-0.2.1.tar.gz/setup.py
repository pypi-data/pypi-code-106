# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zscaler_python_sdk', 'zscaler_python_sdk.lib']

package_data = \
{'': ['*']}

install_requires = \
['black>=21.9b0,<22.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'zscaler-python-sdk',
    'version': '0.2.1',
    'description': 'Unofficial Zscaler API python sdk',
    'long_description': '# Zscaler Python SDK\nThis is a Python SDK for Zscaler Internet Access. This client library is designed to support the Zscaler Internet Access (ZIA) API. Now This library does not support Zscaler Private Access (ZPA), but this will be implemented in the future.\nThis SDK has been developed mainly using Python 3.9.0 .\n\nNOTE: This repository is not official. Zscaler does not support this repository.\n\n## Preparation\nYou need a ZIA credentials like below.\n- ZIA Admin Username (like `admin@example.com`)\n- ZIA Admin Password\n- ZIA Hostname (like `zscaler.net`)\n- ZIA APIKEY (You need to request an api key to Zscaler support team.)\n\n## Set profile\nIf you have verified your credentials, set up your credentials to use this repository. Please replace `/Users/utah18` to your arbitrary directory path.\n\n```\n$ mkdir /Users/utah18/.zscaler && cat > /Users/utah18/.zscaler/config.ini <<EOF\n[zia]\nUSERNAME=example@example.com\nPASSWORD=P@ssw0rd\nHOSTNAME=zscaler.net\nAPIKEY=xxxxxxxxxxxxxxxxxxxxxxx\nEOF\n```\n\n## Clone and Install Repository\nIn this case, we use `poetry`. If you don\'t have this, please install poetry from [HERE](https://python-poetry.org/docs/)\n```\n$ poetry add zscaler-python-sdk\n```\n\n## Quick Start\nAfter installing, you can try below to check if you could use this library.\n```\n$ python\n$ from zscaler_python_sdk.zia import Zia\n$ zia = Zia("/Users/utah18/.zscaler/config.ini")\n$print(zia.fetch_admin_users())\n```\n\n...\nReporting Issues\nIf you have bugs or other issues specifically pertaining to this library, file them here.\n\n## References\n- https://help.zscaler.com/zia/api\n- https://help.zscaler.com/zia/zscaler-api-developer-guide\n- https://help.zscaler.com/zia/sd-wan-api-integration\n',
    'author': 'yuta519',
    'author_email': 'yuta519.ka23tf@docomo.ne.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yuta519/zscaler-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
