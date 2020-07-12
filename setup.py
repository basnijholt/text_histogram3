#!/usr/bin/env python
from setuptools import setup

readme = open("README.rst").read()

setup(
    name="text_histogram3",
    version="1.0.0",
    description="A dependency-free library to quickly make ascii histograms from data.",
    long_description=readme,
    author="Bas Nijholt, Andy Kish, Jehiah Czebotar",
    author_email="bas@nijho.lt",
    url="https://github.com/basnijholt/text_histogram3",
    py_modules=["text_histogram3"],
    license="Apache License, Version 2.0",
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Terminals",
    ],
)
