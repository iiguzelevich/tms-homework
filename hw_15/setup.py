"""A setuptools base setup module
"""
from os import path
from setuptools import setup
from setuptools import find_namespace_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

setup(
    name='my_hw_package',
    version='1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iiguzelevich/tms-homework',
    author='Igor',
    author_email='iiguzelevich@gmail.com',
    package_dir={'': 'my_hw_package'},
    packages=find_namespace_packages(where='my_hw_package'),
    python_requires='>=3.5',
    install_requires=['prettytable']
)

