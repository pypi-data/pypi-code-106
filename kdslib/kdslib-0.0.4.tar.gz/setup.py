from setuptools import setup, find_packages
from distutils.core import setup

VERSION = '0.0.4' 
DESCRIPTION = 'Kiewit Data Services logging and data connection helpers'
LONG_DESCRIPTION = 'Kiewit Data Services logging and data connection helpers'

# Setting up
setup(
       # the name must match the folder name 'kdslib'
        name="kdslib", 
        version=VERSION,
        author="kdslibraries",
        author_email="kdslibraries@aol.com",
        description='Kiewit Data Services logging and data connection helpers',
        long_description='Kiewit Data Services logging and data connection helpers',
        packages=find_packages(),
        install_requires=['msal','requests','sqlalchemy'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'msal'
        
        keywords=['python', 'kdslib'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)