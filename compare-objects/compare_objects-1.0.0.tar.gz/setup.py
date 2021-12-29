import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compare_objects",
    version="1.0.0",
    author="Elyashiv Danino",
    author_email="elyashiv3839@gmail.com",
    description="Resolve schema and deploy to single schema",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/elyashiv3839/compare_objects.git",
    download_url="https://github.com/elyashiv3839/compare_objects/archive/refs/tags/1.0.0.tar.gz",
    project_urls={"Bug Tracker": "https://github.com/elyashiv3839/compare_objects.git"},
    classifier=[
        "Programming Language :: Python :: 3",
        "Operating System :: Multi-platform",
        'License :: OSI Approved :: MIT License',
    ],
    packages=['compare_objects'],
    python_requires=">=3.6",
)
