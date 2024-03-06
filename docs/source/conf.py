# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SteinVI'
copyright = '2024, LuisFiegl'
author = 'LuisFiegl'
release = '06.03.2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys, os
sys.path.insert(0, os.path.abspath('.'))

extensions = ['sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.ipynb']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

