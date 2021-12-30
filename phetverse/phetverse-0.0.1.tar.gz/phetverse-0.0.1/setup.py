import setuptools

setuptools.setup(
    name="phetverse",
    version="0.0.1",
    author="Xiaoyu Zhai",
    author_email="xiaoyu.zhai@hotmail.com",
    description="A placeholder for phetverse project",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "phetverse"},
    packages=setuptools.find_packages(where="phetverse"),
    python_requires=">=3.7",
)