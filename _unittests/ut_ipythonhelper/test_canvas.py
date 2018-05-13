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

from src.code_beatrix.ipythonhelper import display_canvas_point


class TestCanvas(unittest.TestCase):

    def test_canvas(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        points = display_canvas_point('gid')
        self.assertEqual(points, [])


if __name__ == "__main__":
    unittest.main()
