import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phet",
    version="0.0.1",
    author="Xiaoyu Zhai",
    author_email="xiaoyu.zhai@hotmail.com",
    description="A placeholder for phet-project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "phet"},
    packages=setuptools.find_packages(where="phet"),
    python_requires=">=3.7",
)