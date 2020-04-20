# Standard library imports
import os
from setuptools import setup, find_packages


def read(filename):
    with open(filename) as stream:
        return stream.read()


# Read package metadata from __about__.py, to avoid importing the whole
# package prior to installation.
about = dict()
with open(os.path.join("battlemuffin", "__about__.py")) as fp:
    exec(fp.read(), about)
    about = dict((k.strip("_"), about[k]) for k in about)

install_requires = [
    "typing==3.7.4.1",
    "AuthLib==0.14.1",
    "requests==2.23.0",
    "uplink==0.9.1",
]

extras_require = {
    "tests": [
        "pytest==5.4.1",
        "pytest_mock==3.0.0",
        "pytest-cov==2.8.1",
        "syrupy==0.4.1",
        "flake8==3.7.9",
    ],
}

metadata = {
    "author": "Brandon Nelson",
    "author_email": "theredraver@gmail.com",
    "url": "https://github.com/tehmufifnman/BattleMuffin-Python",
    "license": "MIT",
    "description": "A Python implementation of Blizzard's Web API.",
    "long_description": read("README.rst"),
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    "keywords": "blizzard api world-of-warcraft wow python",
    "packages": find_packages(exclude=("tests", "tests.*")),
    "install_requires": install_requires,
    "extras_require": extras_require,
}
metadata = dict(metadata, **about)

if __name__ == "__main__":
    setup(name="battlemuffin", **metadata)
