import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vuln_pillow_wrapper",
    version="0.0.1",
    author="Alberto Fanton",
    author_email="alberto.fanton@conio.com",
    description="A wrapper for a vulnerable pillow version, used for demo purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Conio/vuln_pillow_wrapper",
    project_urls={
        "Bug Tracker": "https://github.com/Conio/vuln_pillow_wrapperhttps/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=['pillow==8.1.0']    
)
