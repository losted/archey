import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Archey",
    version="0.4",
    author="Laurie Clark-Michalek modified by losted",
    author_email="losted@losted.net",
    description="A simple python script to display an Archlinux logo in ASCII art along with basic system information.",
    license="GPL",
    url="http://github.com/losted/archey-git",
    long_description=read("README.md"),
    scripts=["archey"]
)
