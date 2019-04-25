# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import os
import unittest
import shutil
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
from code_beatrix.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
import code_beatrix


class TestLONGNotebookExample (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "jyquickhelper", "ensae_projects"], __file__)

    def test_notebook_example(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_exemples_long")
        keepnote = ls_notebooks("exemples")
        self.assertTrue(len(keepnote) > 0)

        source = os.path.join(os.path.dirname(keepnote[0]), "data")
        data = os.path.join(temp, 'data')
        os.mkdir(data)
        for img in os.listdir(source):
            shutil.copy(os.path.join(source, img), data)

        try:
            res = execute_notebooks(temp, keepnote,
                                    lambda i, n: "poppins" in n,
                                    fLOG=fLOG,
                                    clean_function=clean_function_notebook)
            execute_notebook_list_finalize_ut(
                res, fLOG=fLOG, dump=code_beatrix)
        except Exception as e:  # pylint: disable=W0703
            if "RegexMatchError" not in str(e):
                raise e
            warnings.warn("pytube issue: {}".format(e))
            return


if __name__ == "__main__":
    unittest.main()
