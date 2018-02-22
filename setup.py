import os
from setuptools import setup, find_packages

VERSION = '0.0.1'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='gt-tsp',
    version=VERSION,
    description="Traveling Salesman Problem - Solutions in Python",
    long_description=read('README.md'),
    author='Pramod Kotipalli - School of Interactive Computing - Georgia Institute of Technology',
    author_email='pramodk@gatech.edu',
    url='https://github.com/p13i/Traveling-Salesman-Problem',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)
