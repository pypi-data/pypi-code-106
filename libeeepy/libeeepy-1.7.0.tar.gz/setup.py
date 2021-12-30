import os
from setuptools import setup, find_packages


path = os.path.abspath(os.path.dirname(__file__))

try:
  with open(os.path.join(path, 'README.md')) as f:
    long_description = f.read()
except Exception as e:
  long_description = "customize libeeechina"

setup(
    name = "libeeepy",
    version = "1.7.0",
    keywords = ["data process", "sunshubei", "pymysql","songmeiyang"],
    description = "A public module of eeechina.",
    long_description = long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.6.0",
    license = "MIT Licence",

    url = "https://www.eeechina.cn",
    author = ["sunshubei","songmeiyang"],
    author_email = "sunshubei@outlook.com,songmeiyang@vip.qq.com",

    packages = find_packages(),
    include_package_data = True,
    install_requires = ["numpy", "pandas", "pymysql"],
    platforms = "any",

    scripts = []
)
