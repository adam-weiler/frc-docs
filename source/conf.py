# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./frc-docs/source"))

# -- Project information -----------------------------------------------------

project = "FIRST Robotics Competition"
copyright = "2021, FIRST and other WPILib Contributors"
author = "WPILib"
version = "2021"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_tabs.tabs",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.ghcontributors",
    "sphinxcontrib.rsvgconverter",
    "sphinxext.delta",
    "sphinxext.opengraph",
    "sphinxext.photofinish",
    "sphinxext.rediraffe",
    "sphinxext.remoteliteralinclude",
    "sphinxext.toptranslators",
    "sphinxext.linkcheckdiff",
    "sphinxext.mimictoc",
    "hoverxref.extension",
    "notfound.extension",
    "versionwarning.extension",
    "sphinx_panels",
]

local_extensions = [
    "_extensions.post_process",
]

extensions += local_extensions

versionwarning_messages = {
    "latest": """
        The documentation you are currently viewing is for upcoming changes to WPILib.
        Please see the <a href="https://docs.wpilib.org" id="versionwarning_href">stable</a> version for the current release of WPILib.
        <script>
            document.getElementById("versionwarning_href").setAttribute("href", location.href.replace("/latest/", "/stable/"))
        </script>
        """
}


versionwarning_admonition_type = "warning"
versionwarning_banner_title = "Warning!"
versionwarning_body_selector = 'div[class="document"]'

# Redirect branch
rediraffe_branch = "origin/main"

# File containing redirects
rediraffe_redirects = "redirects.txt"

# Required accuracy for redirect writer
rediraffe_auto_redirect_perc = 80

# Configure linkcheck diff branch
linkcheckdiff_branch = "origin/main"

# Configure OpenGraph support
ogp_site_url = "https://docs.wpilib.org/en/latest/"
ogp_site_name = "FIRST Robotics Competition Documentation"
ogp_image = (
    "https://raw.githubusercontent.com/wpilibsuite/branding/main/png/wpilib-128.png"
)

# Enables ChiefDelphi support
ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
    '<meta name="theme-color" content="#AC2B37" />',
]

# Set location of pages to be indexed by delta
delta_doc_path = "source"

# Enable hover content on glossary term
hoverxref_roles = ["term"]

# TODO Directives omit a warning
todo_emit_warnings = False

# TODO Directives are not shown in output
todo_include_todos = False

# Disable following anchors in URLS for linkcheck
linkcheck_anchors = False

# Linkcheck Exclusions
linkcheck_ignore = [
    r".*kauailabs.com.*",
    r".*wpilibpi.local.*",
    r".*andymark.com.*",
    r".*ti.com/lit/an/spma033a/spma033a.pdf.*",
    r".*wpilibpi.local.*",
]

# Sets linkcheck timeout in seconds
linkcheck_timeout = 30
linkcheck_retries = 3
linkcheck_workers = 1

# Specify a standard user agent, as Sphinx default is blocked on some sites
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"

# Autosection labels prefix document path and filename
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ["docs/beta/*"]

# Specify the master doc file, AKA our homepage
master_doc = "index"

# Specify files to ignore during SizeCheck
IMAGE_SIZE_EXCLUSIONS = [
    "docs/networking/networking-introduction/diagrams/mixing-static-dynamic.drawio.svg",
    "docs/software/vision-processing/wpilibpi/diagrams/vision-code-on-a-coprocessor.drawio.svg",
    "docs/software/vision-processing/introduction/diagrams/vision-code-on-a-coprocessor.drawio.svg",
    "docs/controls-overviews/images/frc-control-system-layout.svg",
]

# Required to display LaTeX in hover content
hoverxref_mathjax = True

# Use MathJax3 for better page loading times
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Sidebar logo
html_logo = "assets/wpilibDocsLogo.png"

# URL favicon
html_favicon = "assets/FIRSTicon_RGB_withTM.ico"

# Specify canonical root
# This tells search engines that this domain is preferred
html_baseurl = "https://docs.wpilib.org/"

html_theme_options = {
    "collapse_navigation": True,
    "sticky_navigation": False,
    "titles_only": True,
}

user_options = [
    ("warning-is-error", True),
]


def setup(app):
    app.add_css_file("css/frc-rtd.css")

    # Local Api Docs support
    app.add_js_file("js/api-docs-redirect.js")

    # Right-to-left support
    is_rtl = app.config.language in rtl_locale
    app.config.hoverxref_tooltip_side = "left" if is_rtl else "right"
    if is_rtl:
        app.add_css_file("css/frc-rtl.css")

    # Fix rtd version/language menu on iOS
    app.add_js_file("js/fix-rtd-menu-ios.js")

    # Launch external links in a new tab/window
    app.add_js_file("js/external-links-new-tab.js")


# -- Options for latex generation --------------------------------------------

latex_engine = "xelatex"

# Disable xindy support
# See: https://github.com/readthedocs/readthedocs.org/issues/5476
latex_use_xindy = False

latex_elements = {
    "fontpkg": r"""
	\setmainfont{DejaVu Serif}
	\setsansfont{DejaVu Sans}
	\setmonofont{DejaVu Sans Mono}""",
    "preamble": r"""
	\usepackage[titles]{tocloft}
	\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
	\setlength{\cftchapnumwidth}{0.75cm}
	\setlength{\cftsecindent}{\cftchapnumwidth}
	\setlength{\cftsecnumwidth}{1.25cm}
	""",
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
    "printindex": r"\footnotesize\raggedright\printindex",
}

suppress_warnings = ["epub.unknown_project_files"]

sphinx_tabs_valid_builders = ["epub", "linkcheck"]


# Options for translation support -------------------------------------------

gettext_compact = False
locale_dirs = ["locale/"]
rtl_locale = ["he"]
