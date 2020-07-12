#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open("README.rst").read()

setup(
    name="text_histogram",
    version="1.0.0",
    description="A dependency-free library to quickly make ascii histograms from data.",
    long_description=readme,
    author="Bas Nijholt, Andy Kish, Jehiah Czebotar",
    author_email="agkish@gmail.com",
    url="https://github.com/Kobold/text_histogram",
    py_modules=["text_histogram"],
    license="Apache License, Version 2.0",
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Terminals",
    ],
)
