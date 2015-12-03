#-*- coding: utf-8 -*-
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
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

import my_hachibee_sphinx_theme as hachibee_sphinx_theme

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
html_title = "lesenfantcodaient.fr"
language = "fr"

blog_root = "http://lesenfantscodaient.fr/"
