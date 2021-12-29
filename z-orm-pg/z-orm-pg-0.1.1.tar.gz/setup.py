from setuptools import setup

setup(
    name='z-orm-pg',
    version='0.1.1',
    author='homo-zhou',
    author_email='408088242@qq.com',
    url='http://127.0.0.1',
    description='An orm for postgresql using peewee',
    packages=['zormpg'],
    install_requires=['psycopg2','peewee'],
    entry_points={
        'console_scripts': []
    }
)