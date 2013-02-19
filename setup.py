# -*- coding: utf-8 -*-
import sys
from setuptools import setup

version = sys.version_info[:2]
install_requires = ['watchdog', 'termcolor']

long_description = """
requirements
------------
* Python 2.7

Feature
-------
* "Sabun" is Simple, Easy and Awesome TODO Task Manager

about detail.
-------------
see github.com_ :).

.. _github.com: https://github.com/esehara/sabun
"""


if version < (2, 7) or (3, 0) <= version <= (3, 1):
    install_requires += ['argparse']

setup(
    name="sabun",
    description="Easy and Simple TODO Task Logger",
    long_description=long_description,
    version="0.1.1",
    license="MIT License",
    author="shigeo esehara",
    author_email="esehara@gmail.com",
    packages=['sabun', ],
    entry_points={'console_scripts': 'sabun=sabun.console:main'},
    install_requires=install_requires)
