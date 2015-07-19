"""
@brief      test log(time=0s)
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


from pyquickhelper import fLOG, explore_folder_iterfile
from pyquickhelper.ipythonhelper import upgrade_notebook
from src.code_beatrix.jsscripts import copy_jstool2ipython


class TestCopyTools(unittest.TestCase):

    def test_copy_tools(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            return

        res = copy_jstool2ipython("snap")
        assert isinstance(res, list)


if __name__ == "__main__":
    unittest.main()
