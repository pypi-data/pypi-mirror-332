# vim: set noexpandtab ts=4 sw=4:
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = emd
SOURCEDIR     = doc/source
BUILDDIR      = doc/build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

version:
	python -c "import emd; print(emd.__version__)"

clean:
	rm -fr build dist emd/_version.py
	rm -fr doc/build
	rm -fr doc/source/emd_tutorials
	rm -fr doc/source/changelog.md
	rm -fr emd.egg-info

install:
	python -m pip install ".[full]"

build: install
	python -m build --wheel --sdist

clean-build: clean install
	python -m build --wheel --sdist

release-build: clean
	# Patch setuptools_scm to create one-time release build with simple version
	sed -i '' 's/python-simplified-semver/only-version/g' pyproject.toml
	python -m build --wheel --sdist
	sed -i '' 's/only-version/python-simplified-semver/g' pyproject.toml

check-dist:
	twine check dist/* --strict

test:
	pytest
	coverage html

doc: doc-html

doc-html:
	sphinx-build -M html doc/source/ doc/build/
	# python3 setup.py build_sphinx -a -E
	cp doc/source/emd_tutorials/*/*ipynb doc/source/_notebooks/

spell:
	codespell -s --ignore-words=ignore_words.txt `find . -type f -name \*.py`

# Make single reqs file for readthedocs
# https://github.com/readthedocs/readthedocs.org/issues/1112
reqs:
	python -c "import emd; emd.support.create_readthedocs_requirements()"

.PHONY: help Makefile
