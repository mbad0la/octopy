from setuptools import setup, find_packages

setup (
    name='octoAPy',
    version='0.0.1',
    description='Github API wrapper for pythonistas',
    url='https://github.com/mbad0la/octoAPy',
    author='Mayank Badola',
    author_email='mbad0la@outlook.com',
    license='MIT',
    packages=find_packages(exclude('tests')),
)
