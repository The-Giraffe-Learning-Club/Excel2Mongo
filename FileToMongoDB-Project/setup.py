#!/usr/bin/env python3

from pathlib import Path

import setuptools

project_dir = Path(__file__).parent

setuptools.setup(
    name="Data_Ingestion",
    version="1.0.0",
    description="File to MongoDB Ingestion Project",
    # Allow UTF-8 characters in README with encoding argument.
    long_description=project_dir.joinpath("README.rst").read_text(encoding="utf-8"),
    keywords=["python"],
    author="Girish",
    url="",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    # pip 9.0+ will inspect this field when installing to help users install a
    # compatible version of the library for their Python version.
    python_requires=">=3.6",
    # There are some peculiarities on how to include package data for source
    # distributions using setuptools. You also need to add entries for package
    # data to MANIFEST.in.
    # See https://stackoverflow.com/questions/7522250/
    include_package_data=True,
    # This file is required to inform mypy that inline type hints are used.
    #   See: https://mypy.readthedocs.io/en/stable/installed_packages.html
    package_data={"data_ingestion": ["py.typed"]},
    # This is a trick to avoid duplicating dependencies between both setup.py and
    # requirements.txt.
    # requirements.txt must be included in MANIFEST.in for this to work.
    # It does not work for all types of dependencies (e.g. VCS dependencies).
    # For VCS dependencies, use pip >= 19 and the PEP 508 syntax.
    #   Example: 'requests @ git+https://github.com/requests/requests.git@branch_or_tag'
    #   See: https://github.com/pypa/pip/issues/6162
    install_requires=project_dir.joinpath("requirements.txt").read_text().split("\n"),
    zip_safe=False,
    entry_points={"console_scripts": ["data_ingestion=data_ingestion.cli:main"]},
)
