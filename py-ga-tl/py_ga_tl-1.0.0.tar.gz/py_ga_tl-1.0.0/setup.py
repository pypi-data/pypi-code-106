import setuptools

setuptools.setup(
    name="py_ga_tl",
    version="1.0.0",
    author="Nguyen Duy Sang",
    author_email="ndsang@ctu.edu.vn",
    description="Sort description",
    long_description="Full description",
    long_description_content_type="text/markdown",
    url="https://github.com/sangduynguyen",
    #packages=setuptools.find_packages(),
    install_requires=[
            'pandas',
            'numpy',
            'matplotlib',
            #'pylab',
            #'tkinter',
            #'builtins',
            #'os',
            #'sys'

        ],
    extras_require={
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ]
)
