from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="test-automata",
    author="Exabyte Inc.",
    author_email="info@exabyte.io",
    url="https://github.com/Exabyte-io/automata",
    description='Exabyte Automated Publishing Sandbox',
    long_description=long_description,
)
