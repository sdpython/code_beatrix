# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""
import os
import unittest
import shutil
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
from code_beatrix.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
import code_beatrix


class TestNotebookExampleVideo (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "jyquickhelper", "ensae_projects"], __file__)

    def test_notebook_example_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            import gizeh
        except ImportError as e:
            warnings.warn('requires Graphviz 2.44 on Windows %r' % e)
            return

        temp = get_temp_folder(__file__, "temp_exemples_video")
        keepnote = ls_notebooks("exemples")
        self.assertTrue(len(keepnote) > 0)

        source = os.path.join(os.path.dirname(keepnote[0]), "data")
        images = os.path.join(temp, 'data')
        os.mkdir(images)
        for img in os.listdir(source):
            shutil.copy(os.path.join(source, img), images)

        if is_travis_or_appveyor() == "circleci":
            def clean(cell):
                cell = clean_function_notebook(cell)
                # ValueError: Cannot embed the 'gif' image format (circleci)
                cell = cell.replace('Image("video.gif")',
                                    '# Image("video.gif")')
                return cell
        else:
            clean = clean_function_notebook

        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "video" in n,
                                fLOG=fLOG, clean_function=clean)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=code_beatrix)


if __name__ == "__main__":
    unittest.main()
