from setuptools import setup, find_packages

long_description= '''Библиотека по числовым методам'''

setup(name='CHISLformal',
      version='0.4',
      url='https://github.com/NooODZy/CHISLformal',
      license='MIT',
      packages=find_packages(),
      author='Fedor987',
      author_email='antonvalentini40@gmail.com',
      install_requires = ['numpy','sympy'],
      zip_safe=False)