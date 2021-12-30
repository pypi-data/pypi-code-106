from setuptools import setup, find_packages

setup(
    name='simple-dbc',
    version='0.0.60',
    description='Simple database client for defining database tables and building queries in object-oriented fashion',
    url='https://github.com/AnthonyRaimondo/simple-dbc',
    author='Anthony Raimondo',
    author_email='anthonyraimondo7@gmail.com',
    license='GNU',
    package_dir={'': 'src/main/python'},
    packages=find_packages(where='src/main/python'),
    include_package_data=True,
    install_requires=['pydantic', 'mysql-connector-python', 'pandaSuit']
)
