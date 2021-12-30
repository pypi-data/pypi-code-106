# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['slotscheck']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1,<5']}

entry_points = \
{'console_scripts': ['slotscheck = slotscheck:cli']}

setup_kwargs = {
    'name': 'slotscheck',
    'version': '0.0.1',
    'description': 'Check the usage of __slots__.',
    'long_description': "✅ Slotscheck\n=============\n\n.. image:: https://img.shields.io/pypi/v/slotscheck.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/slotscheck\n\n.. image:: https://img.shields.io/pypi/l/slotscheck.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/slotscheck\n\n.. image:: https://img.shields.io/pypi/pyversions/slotscheck.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/slotscheck\n\n.. image:: https://img.shields.io/readthedocs/slotscheck.svg?style=flat-square\n   :target: http://slotscheck.readthedocs.io/\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square\n   :target: https://github.com/psf/black\n\nAdding ``__slots__`` to a class in Python is a great way to reduce memory usage.\nBut to work properly, all subclasses need to implement it.\nIt turns out it's easy to forget one class in complex inheritance trees.\nWhat's worse: there is nothing warning you that you messed up.\n\n*Until now!*\n\nQuickstart\n----------\n\nUsage is quick from the command line:\n\n.. code-block:: bash\n\n   slotscheck [MODULE]\n\n\nFor example:\n\n.. code-block:: bash\n\n   $ slotscheck pandas\n   incomplete slots in 'pandas.core.internals.blocks.Block'\n   incomplete slots in 'pandas.core.internals.blocks.NumericBlock'\n   incomplete slots in 'pandas.core.internals.blocks.ObjectBlock'\n   incomplete slots in 'pandas.core.internals.array_manager.SingleArrayManager'\n   incomplete slots in 'pandas.core.internals.managers.SingleBlockManager'\n   incomplete slots in 'pandas.core.internals.array_manager.BaseArrayManager'\n   incomplete slots in 'pandas.core.internals.array_manager.SingleArrayManager'\n   incomplete slots in 'pandas.core.internals.blocks.Block'\n   incomplete slots in 'pandas.core.internals.blocks.CategoricalBlock'\n   incomplete slots in 'pandas.core.internals.blocks.DatetimeLikeBlock'\n   incomplete slots in 'pandas.core.internals.blocks.NumericBlock'\n   incomplete slots in 'pandas.core.internals.blocks.ObjectBlock'\n   incomplete slots in 'pandas.core.internals.managers.BaseBlockManager'\n   incomplete slots in 'pandas.core.internals.managers.SingleBlockManager'\n\nLimitations\n-----------\n\n- Even in the case that slots are not inherited properly,\n  there may still an advantage to using them\n  (i.e. attribute access speed and _some_ memory savings)\n- Only classes at module-level are checked (i.e. no nested classes)\n- In rare cases imports may fail, the module is then skipped. This is logged.\n\nInstallation\n------------\n\nIt's available on PyPI.\n\n.. code-block:: bash\n\n  pip install slotscheck\n",
    'author': 'Arie Bovenberg',
    'author_email': 'a.c.bovenberg@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ariebovenberg/slotscheck',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4',
}


setup(**setup_kwargs)
