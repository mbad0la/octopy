import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
    name='octoAPy',
    version='0.0.1',
    description='Github API wrapper for pythonistas',
    long_description=read('README.rst'),
    url='https://github.com/mbad0la/octoAPy',
    author='Mayank Badola',
    author_email='mbad0la@outlook.com',
    license='MIT',
    packages=find_packages(exclude('tests')),
)
