# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webhook_utils', 'webhook_utils.contrib', 'webhook_utils.crypto']

package_data = \
{'': ['*']}

extras_require = \
{'httpx': ['httpx>=0.21.1,<0.22.0']}

setup_kwargs = {
    'name': 'webhook-utils',
    'version': '0.2.0',
    'description': 'Short, well documented utilities for interacting with webhooks.',
    'long_description': '# Webhook Utils\n\nA set of utilities for interacting with webhooks.\n\n[![Test Webhook Utils](https://github.com/tizz98/webhook-utils/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/tizz98/webhook-utils/actions/workflows/main.yaml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/tizz98/py-paas/tree/main/LICENSE)\n\n## Installation\n\n```shell\npip install webhook-utils\n```\n\n## Usage\n\n### Crypto\n\nAvailable hash algorithms for all methods are:\n- `md5` (not recommended)\n- `sha1`\n- `sha256` (recommended)\n\nLearn more about HMAC signatures [here](https://webhooks.dev/docs/auth/#hmac).\n\n#### Generating HMAC signatures\n\nBare usage:\n```python\nfrom webhook_utils.crypto import generate_sha256_signature\n\nprint(generate_sha256_signature(b\'secret-key\', b\'some-message\'))\n```\n\n#### Comparing HMAC signatures\n\nBare usage:\n```python\nfrom webhook_utils.crypto import compare_sha256_signature\n\nis_valid_signature = compare_sha256_signature(\n    b\'secret-key\',\n    b\'some-message\',\n    \'expected-signature\',\n)\nif not is_valid_signature:\n    raise ValueError(\'Invalid signature\')\n```\n\n### Httpx\n\n`webhook-utils` has a built-in `httpx.Auth` class that can be used to\nautomatically sign requests made with an `httpx.Client`.\n\nAn `X-Webhook-Signature` header will be added to all `POST` requests.\nThe signature will be generated using the `webhook_key` and the\nprovided signature method (defaults to `sha256`).\n\nThe header, signature, and http methods can be customized by passing\nthe `header_name`, `gen_signature_method`, and `methods` keyword arguments.\n\n```shell\npip install webhook-utils[httpx]\n```\n\n```python\nimport httpx\nfrom webhook_utils.contrib.httpx_auth import WebhookAuth\nfrom webhook_utils.crypto import generate_sha1_signature\n\n# Basic usage\nauth = WebhookAuth("secret-key")\nclient = httpx.Client(auth=auth)\n\n\n# Customized usage\nauth = WebhookAuth(\n    "secret-key",\n    header_name="My-Webhook-Signature",\n    gen_signature_method=generate_sha1_signature,\n    methods={"POST", "PUT"},\n)\nclient = httpx.Client(auth=auth)\nclient.post("https://example.com/webhook", json={"foo": "bar"})\n```\n\n## Publishing to PYPI\n\n```shell\npoetry build\n# Verify that everything looks correct on test.pypi.org\npoetry publish -r testpypi\npoetry publish\n```\n',
    'author': 'Elijah Wilson',
    'author_email': 'dev.tizz98@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tizz98/webhook-utils',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
