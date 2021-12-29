# -*- coding: utf-8 -*-
"""Installer for the ruddocom.iframer package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.md').read(),
])


setup(
    name='ruddocom.pdfiframer',
    version='1.0',
    description="PDF IFRAME add-on for Plone",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    ],
    keywords='Python Plone CMS',
    author='Manuel Amador (Rudd-O)',
    author_email='rudd-o+plone@rudd-o.com',
    url='https://github.com/Rudd-O/ruddocom.pdfiframer',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/ruddocom.pdfiframer',
        'Source': 'https://github.com/Rudd-O/ruddocom.pdfiframer',
        'Tracker': 'https://github.com/Rudd-O/ruddocom.pdfiframer/issues',
        # 'Documentation': 'https://ruddocom.policy.readthedocs.io/en/latest/',
    },
    license='GPL version 2 or later',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ruddocom'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'Products.CMFPlone',
        'Products.GenericSetup>=1.8.2',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
