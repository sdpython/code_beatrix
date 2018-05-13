# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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

from src.code_beatrix.ipythonhelper import local_d3js


class TestIpyPath(unittest.TestCase):

    def test_local_d3js(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        r = local_d3js()
        if "http://" not in r:
            assert os.path.exists(r)


if __name__ == "__main__":
    unittest.main()
