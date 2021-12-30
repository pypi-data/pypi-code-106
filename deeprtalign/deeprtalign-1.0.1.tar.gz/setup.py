from setuptools import setup, find_packages


setup(
	name='deeprtalign',
	version="1.0.1",
	packages=find_packages(),
	python_requires='>=3',
	install_requires=[
						'xlrd==1.2.0',
						'pandas>=0.24',
		],

	package_data={
		'deeprtalign': ['data/base.npy','data/params.pt']
		},

	author='Yi Liu',
	author_email='leoicarus@163.com',
	description='retention time alignment tool for large cohort LC-MS data analysis',
	license='GPLv3'
)