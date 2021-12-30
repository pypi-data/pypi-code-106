from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0'
DESCRIPTION = 'Package to convert .py into jupyter executable notebook'
long_description = "head over to https://github.com/arnavrneo/getipynb"
# Setting up
setup(
    name="getipynb",
    version=VERSION,
    author="arnavr",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'jupyter', 'ipython'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)