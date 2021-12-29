from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='balafirstlibrary',
  version='0.0.1',
  description='A very basic maths calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Bala',
  author_email='felas29@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='maths', 
  packages=find_packages(),
  install_requires=[''] 
)