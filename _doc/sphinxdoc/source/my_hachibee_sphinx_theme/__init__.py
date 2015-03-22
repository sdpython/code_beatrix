# -*- coding: utf-8 -*-

""" """

import os

from sphinx.builders.html import StandaloneHTMLBuilder


def get_html_themes_path():
    """Return list of sphinx themes."""
    here = os.path.abspath(os.path.dirname(__file__))
    return here


def setup(app):
    pass
    # script_files = [
    #     '_static/dist/js/jquery.min.js',
    #     '_static/dist/js/underscore-min.js',
    #     '_static/dist/js/doctools.js',
    # ]
    # StandaloneHTMLBuilder.script_files = script_files
