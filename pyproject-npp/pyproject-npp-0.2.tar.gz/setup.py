from setuptools import setup

setup(name='pyproject-npp',
      version='0.2',
      description='Programa per tractament de fitxers.',
      long_description="""
# pyproject-npp
## Informació
- Per executar el programa s'ha de tenir instalat el python versio 3 o mes.
- Requeriments a requirements.txt.
- El fitxer compilar.bat transforma el .py en .pyc que es mes eficient i rapid.
- Executar amb opcio -h per veure mes opcions i funcionalitats.
## Instal·lació
- Utilitzant `pip`
```
pip install pyproject
```
## Ús
- Executar el fitxer `pyproject.py` o `pyproject.cpython-39.pyc` amb les opcions adients

- Opcions
```

```
""",
      long_description_content_type='text/markdown',
      url='https://github.com/NilPujolPorta/pyproject',
      author='Nil Pujol Porta',
      author_email='nilpujolporta@gmail.com',
      license='GNU',
      packages=['pyproject'],
      install_requires=[
          'argparse',
          "setuptools>=42",
          "wheel",
          "Gooey",
          "pytest-shutil"
      ],
	entry_points = {
        "console_scripts": ['pyproject-npp = pyproject.pyproject:main']
        },
      zip_safe=False)
