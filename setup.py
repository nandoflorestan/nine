#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://peak.telecommunity.com/DevCenter/setuptools#developer-s-guide
# from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    url='https://github.com/nandoflorestan/nine',
    name="nine",
    author='Nando Florestan',
    version='0.2',
    license='Public domain',
    packages=find_packages(),
    include_package_data=True,
    author_email="nandoflorestan@gmail.com",
    description="Python 2 and 3 compatibility, "
        "such that your code looks more like Python 3",
    long_description=long_description,
    zip_safe=False,
    test_suite='nine',
    install_requires=[],
    keywords=["python 2", 'python 3', 'compatibility'],
    classifiers=[  # http://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        'License :: Public Domain',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
    ],
)
