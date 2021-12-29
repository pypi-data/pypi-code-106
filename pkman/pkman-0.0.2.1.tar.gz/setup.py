import setuptools
import os, glob
from version import version_up
with open("README.md", "r") as fh:
    long_description = fh.read()

packages=setuptools.find_packages(exclude=['local','local.*'])

print('packages:', packages)

version = version_up()
print("version:", version)
setuptools.setup(
    executable=True,
    name="pkman",  # Replace with your own username
    version=version,
    author="Wang Pei",
    author_email="1535376447@qq.com",
    description="A python package manager inspired by npm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/peiiii/pkman",
    packages=packages,
    package_dir={'pkman': 'pkman'},
    install_requires=[
        'fire',
        'codemaker',
        'codetmpl',
        'build',
        'twine',
        'requests'
                    ],
    entry_points={
        'console_scripts': [
            'pkman = pkman.clitools.cli:main',
            'pkx = pkman.clitools.pkx:main',
        ]
    },
    include_package_data=True,
    package_data={
        'pkman': [
            'data/*', 'data/*/*', 'data/*/*/*', 'data/*/*/*/*', 'data/*/*/*/*/*', 'data/*/*/*/*/*/*',
            'data/*/*/*/*/*/*/*',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)