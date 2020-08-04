import os
from setuptools import setup, find_packages

setup(
    name='sample-app',
    version = '0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=["pyspark==2.4.0", "mistpy==1.1.3"]
)