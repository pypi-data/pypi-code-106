import setuptools, os

setuptools.setup(
    name="example-pkg-naturalett",  # Replace with your own username
    version=os.environ.get("BUILD_VERSION", None),
    author="Foo Bar",
    author_email="lidor.ettinger@example.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    packages=['calculate'],
    include_package_data=True,
    python_requires='>=3.6',
)
