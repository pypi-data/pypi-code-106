import os

import setuptools



with open('README.md') as file:
    read_me_description = file.read()

setuptools.setup(
    name='xstavka_parse_package',
    version='0.25',
    author='hackoff',
    description='this unstable package',
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    packages=['xstavka_parse_package'],
    python_requires='>=3.5',
    install_requires=[
        'bs4',
        'lxml',
        'selenium',
        'webdriver_manager',
    ]

)
