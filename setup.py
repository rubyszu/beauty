# coding: utf-8
from setuptools import setup, find_packages  # noqa: H301

NAME = "ones-api-config"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pyyaml"]

setup(
    name=NAME,
    version=VERSION,
    description="ones-api-config",
    author_email="",
    url="",
    keywords=["config", "utils"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
