#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""

import sys
if sys.version_info[0] < 3:
    raise ImportError("pyensae only works with Python 3")

__version__ = "0.5"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/code_beatrix"
__url__ = "http://lesenfantscodaient/"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#code_beatrix"
__license__ = "BSD License"

from .scratchs import check


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    check()
    return True
