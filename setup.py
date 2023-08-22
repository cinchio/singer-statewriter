#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="singer-statewriter",
    version="0.1.1",
    description="A simple script to capture Singer.io state messages and write them to a state file.",
    author="Cinch",
    url="https://github.com/cinchio/singer-statewriter",
    python_requires='>=3.6.0',
    py_modules=["singer_statewriter"],
    install_requires=[],
    entry_points="""
    [console_scripts]
    singer-statewriter=singer_statewriter:main
    """,
    packages=find_packages(include=['singer_statewriter', 'singer_statewriter.*']),
    #package_data = {
    #    "singer_statewriter": ["schemas/*.json"]
    #},
    #include_package_data=True,
)
