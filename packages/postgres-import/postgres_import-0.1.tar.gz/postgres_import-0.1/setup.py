# setup.py

from setuptools import setup, find_packages

setup(
    name="postgres_import",
    version="0.1",
    packages=find_packages(),  # Automatically find packages in the directory
    description="A simple Python package with a function to import data from Excel sheets into created empty tables in Postgresql",
    author="Olu Ayinde",
    author_email="aolufeyijimi@gmail.com",
    #url="https://github.com/yourusername/my_package",  # Optional
    install_requires=[
        "sqlalchemy>=2.0.38",
        "pandas>=2.0.3",
    ],  # List dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)