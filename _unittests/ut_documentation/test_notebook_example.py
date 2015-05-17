#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
import re

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper

from pyquickhelper import fLOG, get_temp_folder
from src.code_beatrix.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook, unittest_raise_exception_notebook


class TestNotebookExample (unittest.TestCase):

    def test_notebook_example(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_exemples")
        keepnote = ls_notebooks("exemples")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        unittest_raise_exception_notebook(res, fLOG)

if __name__ == "__main__":
    unittest.main()
