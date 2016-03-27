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
__license__ = "MIT License"
__blog__ = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "rss_blog_list.xml"))


def _setup_hook(add_print=False, unit_test=False):
    """
    if this function is added to the module,
    the help automation and unit tests call it first before
    anything goes on as an initialization step.
    It should be run in a separate process.

    @param      add_print       print *Success: _setup_hook*
    @param      unit_test       used only for unit testing purpose
    """
    # we can check many things, needed module
    # any others things before unit tests are started
    if add_print:
        print("Success: _setup_hook")


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    from .scratchs import check
    check()
    return True


def load_ipython_extension(ip):
    """
    to allow the call ``%load_ext code_beatrix``

    @param      ip      from ``get_ipython()``
    """
    from .ipythonhelper.magic_scratch import register_scratch_magics
    register_scratch_magics(ip)


try:
    from IPython import get_ipython
    ip = get_ipython()
    if ip is not None:
        import pyquickhelper
        pyquickhelper.load_ipython_extension(ip)
        load_ipython_extension(ip)

except ImportError as e:
    # IPython is not installed
    pass
