===========================
Python Package Cookiecutter 
===========================
Cookiecutter template for a Python package.

* GitHub repo: https://github.com/jdongian/cookiecutter-pypackage/
* Free software: BSD license


Features
--------
* Good requirements handling with parsing from ``requirements.txt`` and ``requirements_dev.txt`` files
* ``# -*- coding: utf-8 -*-`` headers
* ``unittest`` test boilerplate
* tiny ``argparse`` shim
* ``tox`` to set up testing matrix for multiple python versions
* Sphinx docs: Documentation ready for generation with, for example, ReadTheDocs


Usage
-----
Install latest Cookiecutter (requires Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate Python package template::

    cookiecutter https://github.com/jdongian/cookiecutter-pypackage.git


About
-----
Based loosely on https://github.com/audreyr/cookiecutter
