import setuptools


setuptools.setup(
    name="DDetector",
    version="0.0.3",
    author="Jones Lin",
    author_email="jonneslin@gmail.com",
    description="Data distribution detector",
    url="https://github.com/JonnesLin/distribution_detection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'scikit-learn'
    ]
)