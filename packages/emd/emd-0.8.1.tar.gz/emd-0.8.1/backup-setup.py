#!/usr/bin/python

# vim: set expandtab ts=4 sw=4:

"""Configure EMD package and installation."""

import pathlib

from setuptools import setup

# Scripts
scripts = []

name = 'emd'

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Read version
version = (HERE / "emd" / '_version.py').read_text().split(' = ')[1].rstrip('\n').strip("'")
release = version

# Read requirements
reqs = (HERE / "requirements.txt").read_text()
dev_reqs = (HERE / "requirements_dev.txt").read_text()
doc_reqs = (HERE / "requirements_doc.txt").read_text()

# Main setup
setup(
    name=name,

    version=release,

    description='Empirical Mode Decomposition',

    # Author details
    author='Andrew Quinn <a.quinn@bham.ac.uk>',
    author_email='a.quinn@bham.ac.uk',

    long_description=README,
    long_description_content_type="text/markdown",

    # Choose your license
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],

    keywords='EMD Spectrum Frequency Non-Linear Holospectrum Hilbert-Huang',

    packages=['emd'],

    python_requires='>3.9',

    install_requires=reqs,

    extras_require={
        'dev': dev_reqs,
        'doc': doc_reqs,
        'full': dev_reqs + doc_reqs,
    },

    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', name),
            'release': ('setup.py', name)}},
)
