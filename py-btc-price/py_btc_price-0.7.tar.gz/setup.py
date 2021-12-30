from setuptools import setup, find_packages

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.7'
DESCRIPTION = 'Get the current Bitcoin Price or Convert the fiat USD equivalente to BTC.'

setup(
    name = 'py_btc_price',
    packages = ['py_btc_price'],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = 'Eduardo Ismael García Pérez',
    author_email = 'eduardo78d@gmail.com',
    url = 'https://github.com/eduardogpg/py_btc_price',
    keywords = ['Criptocurrency', 'BTC', 'Bitcoin Price', 'BTC price'],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)