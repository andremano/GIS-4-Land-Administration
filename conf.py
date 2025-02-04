# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
sphinx_outputdir = "_build/html"

# -- Project information -----------------------------------------------------

project = 'GIS for Land Administration'
copyright = '2020, Andre da Silva Mano'
author = 'Andre da Silva Mano'

# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
             'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = '[en]'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#in readthedocs.org there occurs "contents.rst not found" error. The master document has to be specified to avoid that error
master_doc = 'index'

#this is to allow figure numbering and referencing
numfig = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"


###########################################################
# Target link-files
link_file = ['_build/assets/ltb-links-gis.rst',
            '_build/assets/data-links-gis.rst'
            ]

# Allows storing external links in separated rst
rst_epilog=""

# Read links in the from the target files
for file in link_file:
    with open(file) as f:
        rst_epilog += f.read()
############################################################

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Set the output directory for Sphinx
if os.environ.get('READTHEDOCS') == 'True':
    html_output_dir = os.path.join(os.environ.get('READTHEDOCS_OUTPUT'), 'html')
else:
    html_output_dir = '_build/html'  # Default local build directory


# Configure paper size, font size, preamble options, etc.
latex_elements = {
    'figure_align': 'H',
    'preamble': '''
        \\usepackage{float}
        ''',
}


