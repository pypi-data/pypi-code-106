from setuptools import setup, find_packages

setup(
    name='simple-dbc',
    version='0.0.59',
    description='Database Client',
    url='https://github.com/AnthonyRaimondo/dbc',
    author='Anthony Raimondo',
    author_email='anthonyraimondo7@gmail.com',
    license='GNU',
    package_dir={'': 'src/main/python'},
    packages=find_packages(where='src/main/python'),
    include_package_data=True,
    install_requires=['pydantic', 'mysql-connector-python', 'pandaSuit']
)
