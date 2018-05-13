# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut

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


from src.code_beatrix.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
import src.code_beatrix


class TestLONGNotebookScratch(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "ensae_projects",
                                         "jyquickhelper"], __file__, hide=True)

    def test_long_notebook_scratch(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_scratch")
        keepnote = ls_notebooks("scratch")
        self.assertTrue(len(keepnote) > 0)
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.code_beatrix)


if __name__ == "__main__":
    unittest.main()
