Utility to translate Snakemake codebase into sphinx-like rst files
==================================================================

.. image:: git@git.km3net.de:km3py/smk2rst.git/badges/master/pipeline.svg
    :target: git@git.km3net.de:km3py/smk2rst.git/pipelines

.. image:: git@git.km3net.de:km3py/smk2rst.git/badges/master/coverage.svg
    :target: https://vpestel.pages.km3net.de/smk2rst/coverage

.. image:: https://git.km3net.de/examples/km3badges/-/raw/master/docs-latest-brightgreen.svg
    :target: https://vpestel.pages.km3net.de/smk2rst


Installation
~~~~~~~~~~~~

It is recommended to first create an isolated virtualenvironment to not interfere
with other Python projects::

  git clone git@git.km3net.de:km3py/smk2rst.git
  cd smk2rst
  python3 -m venv venv
  . venv/bin/activate

Install directly from the Git server via ``pip`` (no cloneing needed)::

  pip install git+git@git.km3net.de:km3py/smk2rst.git

Or clone the repository and run::

  make install

To install all the development dependencies, in case you want to contribute or
run the test suite::

  make install-dev
  make test


---

*Created with ``cookiecutter https://git.km3net.de/templates/python-project``*
