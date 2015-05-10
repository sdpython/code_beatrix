#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""
import os

__version__ = "0.5"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/code_beatrix"
__url__ = "http://lesenfantscodaient/"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#code_beatrix"
__license__ = "BSD License"
__blog__ = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "rss_blog_list.xml"))


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

try:
    from IPython import get_ipython
    from .ipython_helper.magic_scratch import register_scratch_magics

    ip = get_ipython()
    if ip is not None:
        # the program is not run from a notebook
        register_scratch_magics()
except ImportError as e:
    # IPython is not installed
    pass
