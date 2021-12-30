from setuptools import find_packages, setup
with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
    name='claming',
    packages=find_packages(),
    version='1.5',
    description='A Python package for Cleansing Matching',
    author='agistyaanugrah',
    license='MIT',
    install_requires=['strsimpy'],
    long_description=long_description,
    long_description_content_type="text/markdown",
)