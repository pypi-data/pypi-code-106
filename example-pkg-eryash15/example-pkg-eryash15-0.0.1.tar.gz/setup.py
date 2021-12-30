import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-eryash15",
    version="0.0.1",
    author="Yash Gupta",
    author_email="eryash15@gmail.com",
    description="A small example package  by Yash Gupta",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eryash15",
    project_urls={
        "Bug Tracker": "https://github.com/eryash15/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)