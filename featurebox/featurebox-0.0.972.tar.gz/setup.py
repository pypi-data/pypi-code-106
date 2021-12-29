#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# @Time   : 2019/8/2 15:47
# @Author : Administrator
# @Software: PyCharm
# @License: BSD 3-Clause

from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='featurebox',
    version='0.0.972',
    keywords=['features', "combination", "selection"],
    description='This is an box contains tools for machine learning.'
                'Some of code are non-originality, just copy for use. All the referenced code are marked,'
                'details can be shown in their sources',
    install_requires=['pandas', 'numpy', 'sympy', 'scipy', 'scikit-learn', 'joblib', 'matplotlib','deprecated',
                      'requests', 'tqdm', 'six', "featurebox", "pymatgen", "deap", "numba", "ase"],
    include_package_data=True,
    author='wangchangxin',
    author_email='986798607@qq.com',
    python_requires='>=3.6',
    url='https://github.com/boliqq07/featurebox',
    maintainer='wangchangxin',
    platforms=[
        "Windows",
        "Unix",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

    packages=find_packages(
        exclude=["test", "*.test", "*.*.test", "*.*.*.test",
                 "test*", "*.test*", "*.*.test*", "*.*.*.test*", "Instances", "Instance*"],
    ),
    long_description=long_description,
    long_description_content_type='text/markdown'
)
