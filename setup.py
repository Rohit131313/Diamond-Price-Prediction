from setuptools import find_packages,setup
from typing import List


setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='rohit',
    author_email='abc@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)