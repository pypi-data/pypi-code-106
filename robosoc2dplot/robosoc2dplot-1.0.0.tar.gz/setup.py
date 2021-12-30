# to install (be sure to have robosoc2d installed previously):
# python3 setup.py install
#
# to uninstall:
# pip uninstall robosoc2dplot

import setuptools

setuptools.setup(
    name="robosoc2dplot", # Replace with your own username
    version="1.0.0",
    author="Ruggero Rossi",
    author_email="r.rossi@opencomplexity.com",
    description="Draw robosoc2d with matplotlib",
    long_description="Draw robosoc2d with matplotlib",
    long_description_content_type="text/markdown",
    url="https://github.com/rug",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['matplotlib','robosoc2d'],
)