import setuptools
from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
#requirements = ["requests<=2.21.0"]
setup(
    name='tiletool',
    version='0.9.1',
    packages=setuptools.find_packages(),
    url='https://github.com/gibon228/tiletool',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Vincent Vega',
    author_email='kharitonov.oe@gmail.com',
    python_requires='>=3.5',
    description='TileTool is a simple, base module for working with tiles, based on pygame.sprite.Sprite. With TileTool you can transfer tile-levels and drawings from different format files to tile games created on pygame. Имеется документация на русском.',
    #install_requires=requirements,
)





