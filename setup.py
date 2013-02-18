# -*- coding: utf-8 -*-
import sys
from setuptools import setup

version = sys.version_info[:2]
install_requires = ['watchdog']

if version < (2, 7) or (3, 0) <= version <= (3, 1):
    install_requires += ['argparse']

setup(
    name="sabun",
    description="Easy and Simple TODO Task Logger",
    version="0.1",
    licence="MIT License",
    author="shigeo esehara",
    author_email="esehara@gmail.com",
    packages=['sabun', ],
    entry_points={'console_scripts': 'sabun=sabun.console:main'},
    install_requires=install_requires)