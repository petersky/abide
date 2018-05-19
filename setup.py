from __future__ import with_statement
import sys
from setuptools import setup, find_packages

__version__ = None
with open('abide/__init__.py') as f:
    exec(f.read())

# To install the twilio-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name = "abide",
    version = __version__,
    description = "Abide enhanced object persistence",
    author = "Kyle Petersen",
    author_email = "petersky@gmail.com",
    url = "https://github.com/petersky/abide/",
    keywords = ["abide","python"],
    install_requires = [
        "six",
        "pytz",
        "PyJWT >= 1.4.2",
    ],
    extras_require={
        ':python_version<"3.0"': [
            "requests[security] >= 2.0.0",
        ],
        ':python_version>="3.0"': [
            "requests >= 2.0.0",
            "pysocks",
        ],
    },
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
    Abide Enhanced Object Persistence Python Library
    ------------------------------------------------

    DESCRIPTION
    The Abide Python library provides an opinionated approach for serializing,
    exchanging, and persisting Python objects. See
    https://www.github.com/petersky/abide/ for more information.

    LICENSE Abide is distributed under the Apache Software License.
    """ )