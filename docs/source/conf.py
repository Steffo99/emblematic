# Extended Sphinx configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html


###########
# Imports #
###########

import datetime


###########################
# Developer configuration #
###########################
# Alter these to reflect the nature of your project!

# Project name
project = 'emblematic'
# Project author
author = 'Stefano Pigozzi'
# Project copyright
project_copyright = f'{datetime.date.today().year}, {author}'

# Sphinx language
language = "en"

# Configuration for the theme
html_theme_options = {
    # Set this to the main color of your project
    "style_nav_header_background": "#175d36",
}
html_context = {
    "display_github": True,
    # Set this to the name of the organization this GitHub repository is in
    "github_user": "Steffo99",
    # Set this to the name of this repository
    "github_repo": "emblematic",
    # Set this to the name of the main branch slash docs slash
    "github_version": "main/docs/",
}


##########################
# Advanced configuration #
##########################
# Change these options only if you need further customization

# Sphinx extensions
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
]

# Source files encoding
source_encoding = "UTF-8"
# Source file extensions
source_suffix = {
    ".rst": "restructuredtext",
}
# Source files parsers
source_parsers = {}

# The doc from which to start rendering
root_doc = "index"
# Files to ignore when rendering
exclude_patterns = [
    "build",
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
# Sphinx template files
templates_path = [
    '_templates',
]

# Prologue of all rst files
rst_prolog = """
.. |this| replace:: :mod:`emblematic`
"""
# Epilogue of all rst files
rst_epilog = """"""

# Default domain
primary_domain = "py"
# Default role
default_role = "any"

# Print warnings on the page
keep_warnings = False
# Display more warnings than usual
nitpicky = False

# Intersphinx URLs
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.10", None),
    "poetry": 
}
# Manpages URL
manpages_url = "https://man.archlinux.org/"

# HTML builder theme
html_theme = 'sphinx_rtd_theme'
# Title of the HTML page
html_title = f"{project}"
# Short title of the HTML page
html_short_title = f"{project}"
# Path of the documentation static files
html_static_path = [
    "_static",
]
# Path of extra files to add to the build
html_extra_path = [
    "_extra",
]
# Disable additional indexes
html_domain_indices = False

# LaTeX rendering engine to use
latex_engine = "lualatex"
# LaTeX top level title type
latex_toplevel_sectioning = "chapter"
# LaTeX URLs rendering
latex_show_urls = "footnote"
# LaTeX theme
latex_theme = "manual"

# TODOs
todo_include_todos = True
todo_emit_warnings = True
todo_link_only = False

# Smartquotes
smartquotes_excludes = {
    "languages": [
        # Smartquotes is completely broken in italian!
        "it",
        # Keep the default, just in case
        "ja",
    ],
    "builders": [
        "man",
        "text",
    ]
}

# Autodoc
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}
