from setuptools import setup, find_packages
from komlib import *

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='komlib',  # Required
    version='v0.1',  # Required
    description='Kompas python cloud library',  # Required
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kompas ML team',  # Optional
    author_email='fatchur.rahman1@gmail.com', #optional
    packages=["komlib", 
              "komlib.aws"],  # Required
)