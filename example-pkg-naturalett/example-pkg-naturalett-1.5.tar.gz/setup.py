import setuptools, os

setuptools.setup(
    name="example-pkg-naturalett",  # Replace with your own username
    version=os.environ.get("BUILD_VERSION"),
    author="Foo Bar",
    author_email="lidor.ettinger@example.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    scripts=['calculate/calc.py'],
    python_requires='>=3.9',
)
