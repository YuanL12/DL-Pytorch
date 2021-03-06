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
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Personal Notes'
copyright = '2021, Yuan'
author = 'Yuan Luo'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------
# sidebar and website title 
html_title = "Yuan Luo's Note"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    
    # parser markdown file
    'myst_parser',
    # show duration of making html
    'sphinx.ext.duration',

    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    # External stuff
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'py'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'py'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"


html_theme_options = {
    # hide sidebar name
    "sidebar_hide_name": False,

    ## Theme options for 'sphinx_book_theme'
    # # Github icon on the header
    # "repository_url": "https://github.com/YuanL12/DL-Pytorch",
    # "use_repository_button": True,
    # # colab button
    # "launch_buttons": {
    #     "colab_url": "https://{your-colab-url}"
    # },    
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# logos store in the _static folder
# logo appeared in side bar 
# html_logo = "_static/pytorch-logo.png"
# logo apperaed as favicon
html_favicon = "_static/yuan.ico"


#
# -- Options for extlinks ----------------------------------------------------
#
extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# #
# # -- Options for intersphinx -------------------------------------------------
# #
# intersphinx_mapping = {
#     "python": ("https://docs.python.org/3", None),
#     "sphinx": ("https://www.sphinx-doc.org/en/master", None),
# }

#
# -- Options for TODOs -------------------------------------------------------
#
todo_include_todos = True

#
# -- Options for Markdown files ----------------------------------------------
#
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
]
myst_dmath_double_inline = True 
myst_heading_anchors = 3