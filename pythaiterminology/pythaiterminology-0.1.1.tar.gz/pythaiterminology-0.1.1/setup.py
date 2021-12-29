from setuptools import find_packages, setup
setup(
    name='pythaiterminology',
    version='0.1.1',
    description='Thai terminology corpus library',
    author='Chayoot Kosiwanich',
    author_email='khunfloat@gmail.com',
    license='MIT',
    url='https://github.com/khunfloat/pythaiterminology',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)