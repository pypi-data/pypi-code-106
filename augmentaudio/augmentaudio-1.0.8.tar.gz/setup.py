from setuptools import setup, find_packages
from setuptools.command.develop import develop
from distutils.command.install import install as _install
from subprocess import check_call

import sys, os 

def installing(dir):
    from subprocess import call
    call([sys.executable, 'setup_augmentor.py'],
         cwd=os.path.join(dir, 'augaudio'))

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(installing, (self.install_lib,))

with open('README.md') as f:
    long_description = f.read()

setup(
    cmdclass={'install': install},
    name="augmentaudio",
    version="1.0.8",
    author="Bastian Schwickert",
    author_email="Bastian.Schwickert@gmail.com",
    description="A simple audio data augmentation package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://basti564.github.io",
    project_urls={
        "Bug Tracker": "https://github.com/Basti564/augaudio/issues",
        "Source Code": "https://github.com/Basti564/augaudio",
    },
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
          'numpy >= 1.16.2',
          'librosa >= 0.7.2',
          'torch >= 1.7.1',
          ],
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"Topic :: Scientific/Engineering",
    ],
    entry_points={
        "console_scripts": [
            "augaudio=augaudio.cli:main",
        ]
    },
)
