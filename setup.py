# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='htwarfare',
    version='0.1.0',
    description='An http based game',
    long_description=readme,
    author='Zak Kohler',
    author_email='git@y2kbugger.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
