from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='akeuroo-deck',
    version='2.0.1',
    description='A model of a card pack consisting with good features. GitHub: https://github.com/akeuroo/card-deck',
    long_description=open('README.txt').read() + '\n\n' + "Change Log\n==========\n\n2.0.1 (2021-12-29)\n------------------\n- First Release",
    url='',
    author="akeuroo",
    author_email="akeuroo09@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["game", "card", "card game", "card deck", "cards", "deck"],
    packages=find_packages(),
    install_requires=['']
)