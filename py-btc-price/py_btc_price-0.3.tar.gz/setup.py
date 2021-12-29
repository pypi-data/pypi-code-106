from distutils.core import setup

setup(
    name = 'py_btc_price',
    packages = ['py_btc_price'],
    version = '0.3',
    license='MIT',
    description = 'Get the current Bitcoin Price or Convert the fiat USD equivalente to BTC.',
    author = 'Eduardo Ismael García Pérez',
    author_email = 'eduardo78d@gmail.com',
    url = 'https://github.com/eduardogpg/py_btc_price',
    download_url = 'https://github.com/eduardogpg/py_btc_price/archive/refs/tags/0.3.tar.gz',
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
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    ],
)