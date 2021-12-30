from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='batch_async_http',
    version='0.0.1',
    packages=['batch_async_http'],
    url='https://https://github.com/MiesnerJacob/batch_async_http',
    license='GPLv3',
    author='Jacob Miesner',
    author_email='miesner.jacob@gmail.com',
    description='Decorator for async batch calling via http requests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    include_package_data=True,
    keywords=[
        'async',
        'batch',
        'http',
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    install_requires=[
        'requests',
        'asyncio'
    ]
)
