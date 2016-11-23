import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "octopy",
    version = "1.0.0",
    author = "Mayank Badola",
    author_email = "badola21295@gmail.com",
    description = ("Python wrapper for GitHub API"),
    license = "MIT",
    keywords = "github api wrapper python v3",
    url = 'https://github.com/mbad0la/octopy',
    download_url = 'https://github.com/mbad0la/octopy/tarball/1.0.0',
    packages=['octopy'],
    long_description=read('README.rst'),
    install_requires=['requests'],
)
