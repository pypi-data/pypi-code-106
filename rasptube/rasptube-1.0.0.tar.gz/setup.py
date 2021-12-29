from setuptools import setup
  
# specify requirements of your package here
REQUIREMENTS = ['os']
  
# some more details
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    ]
  
# calling the setup function 
setup(name='rasptube',
      version='1.0.0',
      description='a module that creates Youtube links that are capable of running on the raspberry pi',
      author='Walter James Hare',
      packages=['rasplinkgen'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='youtube raspberrypi raspberry pi link url compatable'
      )