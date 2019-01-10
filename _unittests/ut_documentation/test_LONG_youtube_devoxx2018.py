# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
import shutil
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


class TestLONGYoutubeNotebookDevoxx2018(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "jyquickhelper", "ensae_projects"], __file__)

    def test_notebook_example(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_exemples_long_devoxx")
        keepnote = ls_notebooks(os.path.join("ateliers", "devoxx2018"))
        self.assertTrue(len(keepnote) > 0)

        sources = [os.path.join(os.path.dirname(keepnote[0]), "finlaby.jpg")]
        for img in sources:
            shutil.copy(img, temp)

        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "devoxx" in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.code_beatrix)


if __name__ == "__main__":
    unittest.main()
