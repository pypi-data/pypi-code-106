#!/usr/bin/python3

from setuptools import setup, find_packages
import os


setup(name='provis',
      version='0.0.1',
      description='Protein Visualization Library in Python',
      url='https://github.com/czirjakkethz/provis',
      author='Kristof Czirjak',
      author_email='czirjakk@student.ethz.ch',
      license='MIT',
      packages=find_packages(),
      install_requires=['biopython', 'trimesh', 'pyvista', 'biopandas', 'torch', 'pyvtk', 'open3d'],
      keywords=['python', 'protein', 'visualization', 'pdb'],
      zip_safe=False,

)
