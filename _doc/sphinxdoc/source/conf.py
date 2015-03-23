#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  documentation build configuration file, created by
# sphinx-quickstart on Fri May 10 18:35:14 2013.
#

import sys
import os
import datetime
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "code_beatrix")))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

#import my_hachibee_sphinx_theme as hachibee_sphinx_theme
import hachibee_sphinx_theme as hachibee_sphinx_theme

from pyquickhelper.helpgen.default_conf import set_sphinx_variables


set_sphinx_variables(__file__,
                     "Les enfants codaient",
                     "Xavier Dupré",
                     2015,
                     "hachibee",
                     hachibee_sphinx_theme.get_html_themes_path(),
                     locals(),
                     add_extensions=['hachibee_sphinx_theme'])

html_show_copyright = False
