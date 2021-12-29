# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['check_git_repos']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.24,<4.0.0']

entry_points = \
{'console_scripts': ['check_git_repos = check_git_repos:main']}

setup_kwargs = {
    'name': 'check-git-repos',
    'version': '1.0.0',
    'description': 'A command line interface to check git repositories within a directory',
    'long_description': "# check_git_repos\n\nA simple utility script to check git repos contained underneath a given directory, reporting if any of the repos contain changes that\nneed to be upstreamed.\n\n## Usage\n\n```bash\nusage: check_git_repos [-h] [--include-hidden] [path]\n\nCheck the status of git repositories in a directory\n\npositional arguments:\n  path              if given, the directory to start looking from, otherwise the directory will be used\n\noptional arguments:\n  -h, --help        show this help message and exit\n  --include-hidden  whether to look in hidden directories\n```\n\n## Checked issues:\n### Repo level issues:\n- `untracked_files` the repo has files which aren't tracked\n- `dirty_files` the repo has dirty files which need to be committed\n\n### Branch level issues:\nThe reporting format is `branch_issues: [branch] ([issue])`\n\n- `missing_upstream` a branch exists that has no upstream\n- `unpushed_changes` a branch has commits that don't exist upstream\n\n## Development\n\nThe project is built using [poetry](https://github.com/python-poetry/poetry), and has a makefile for development:\n\n- `clean`: clean up build artifacts\n- `develop`: install the project to a virtual environment\n- `format`: format files using black\n- `publish`: publish the project to pypi (given you have credentials)\n\nOnce `make develop` is run, you can run the development version with `poetry run check_git_repos`\n",
    'author': 'Ben Ryves',
    'author_email': 'bryves@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getyourguide/check-git-repos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
