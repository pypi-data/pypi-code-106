""" Setup file for storge """

from setuptools import setup

setup(
    scripts = ['storge', 'storged', 'torge'],
    include_package_data=True,
    package_data={'': ['style.css','favicon.ico']},
)
