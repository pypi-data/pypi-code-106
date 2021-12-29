# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webhook_utils', 'webhook_utils.crypto']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'webhook-utils',
    'version': '0.1.0',
    'description': 'Short, well documented utilities for interacting with webhooks.',
    'long_description': "# Webhook Utils\n\nA set of utilities for interacting with webhooks.\n\n## Installation\n\n```shell\npip install webhook-utils\n```\n\n## Usage\n\n### Crypto\n\nAvailable hash algorithms for all methods are:\n- `md5` (not recommended)\n- `sha1`\n- `sha256` (recommended)\n\nLearn more about HMAC signatures [here](https://webhooks.dev/docs/auth/#hmac).\n\n#### Generating HMAC signatures\n\nBare usage:\n```python\nfrom webhook_utils.crypto import generate_sha256_signature\n\nprint(generate_sha256_signature(b'secret-key', b'some-message'))\n```\n\n#### Comparing HMAC signatures\n\nBare usage:\n```python\nfrom webhook_utils.crypto import compare_sha256_signature\n\nis_valid_signature = compare_sha256_signature(\n    b'secret-key',\n    b'some-message',\n    'expected-signature',\n)\nif not is_valid_signature:\n    raise ValueError('Invalid signature')\n```\n\n## Publishing to PYPI\n\n```shell\npoetry build\n```\n",
    'author': 'Elijah Wilson',
    'author_email': 'dev.tizz98@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tizz98/webhook-utils',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
