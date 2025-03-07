# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib

# -- Project information -----------------------------------------------------
# Add the root folder (up two from conf.py) to avoid Import Errors.
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parents[3]))

# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PHX"
copyright = "2022, bldgtyp, llc"
author = "PH-Tools"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.napoleon"]


templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
