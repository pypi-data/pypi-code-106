from setuptools import setup, find_packages

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="e2L", 
        version='0.0.2',
        license='MIT',
        author="Raphaël Nussbaumer",
        author_email="<rafnuss@gmail.com>",
        description='Generate custom PDF checklists with eBird occurrence data.',
        long_description='eBirdToLaTex Checklist Generator is a Python module which generates a customisable bird checklist based on a specific dataset downloaded from eBird.',
        url="https://github.com/Zoziologie/ebird2latex",
        download_url="https://github.com/Zoziologie/ebird2latex/archive/refs/tags/v0.0.1.tar.gz",
        packages=find_packages(),
        install_requires=['requests'],
        
        keywords=['python', 'eBird', 'LaTeX'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)