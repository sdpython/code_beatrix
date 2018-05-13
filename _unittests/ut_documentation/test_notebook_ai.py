# -*- coding: utf-8 -*-
"""
@brief      test log(time=80s)
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


class TestNotebookAi(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "ensae_projects",
                                         "jyquickhelper"], __file__, hide=True)

    def test_notebook_ai(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_ai")
        keepnote = ls_notebooks("ai")
        self.assertTrue(len(keepnote) > 0)

        source = os.path.join(os.path.dirname(keepnote[0]), "images")
        images = os.path.join(temp, 'images')
        os.mkdir(images)
        for img in os.listdir(source):
            shutil.copy(os.path.join(source, img), images)

        res = execute_notebooks(temp, keepnote, lambda i, n: True, fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.code_beatrix)


if __name__ == "__main__":
    unittest.main()
