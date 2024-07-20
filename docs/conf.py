# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'brother_ql_next'
copyright = '2024 brother_ql_next Contributors.'
author = 'LunarEclipse'
release = '0.11.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

templates_path = ['templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# SphinxAwesome Theme: https://sphinx-themes.org/sample-sites/sphinxawesome-theme/
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'

html_static_path = ['static']
html_css_files = [
    'custom.css',
]


# -- Options for InterSphinx -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}
intersphinx_timeout = 30

# -- Options for AutoDoc -----------------------------------------------------
import os, sys
sys.path.insert(0, os.path.abspath('..'))
#autodoc_member_order = "bysource"
#autodoc_typehints = "description"
#autodoc_preserve_defaults = True
#autodoc_class_signature = "separated"
