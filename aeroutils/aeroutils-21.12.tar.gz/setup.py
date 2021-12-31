#!/usr/bin/env python
"""
Setup file for aeroutils.
"""

from setuptools import setup

from src.aeroutils import __version__, __author__

if __name__ == "__main__":
    with open('README.rst', 'r') as file:
        long_description_ = file.read()

    setup(
        name='aeroutils',
        version=__version__,
        packages=['src/aeroutils',],
        description="Importable utilities for aerospace problem solving.",
        long_description=long_description_,
        license="MIT License",
        url="https://github.com/MattCJones/aeroutils",
        author=__author__,
        author_email='matt.c.jones.aoe@gmail.com',
        scripts=None,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering",
            "Topic :: Utilities",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            ],
        keywords="utility aerospace engineering design problem solving",
        install_requires=('pint', 'numpy'),
    )
