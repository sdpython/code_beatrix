#-*- coding: utf-8 -*-
"""
@brief      test log(time=4s)
"""

import sys
import os
import unittest


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
    import pyquickhelper as skip_
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
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv
from src.code_beatrix.algorithm.data import load_prenoms_w
from src.code_beatrix.algorithm.classroom import random_positions, plot_positions


class TestClassRoom(unittest.TestCase):

    def test_names(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        names = load_prenoms_w()
        self.assertEqual(len(names), 50)

    def test_random_position(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        positions = random_positions(24)
        self.assertEqual(len(positions), 24)

        temp = get_temp_folder(__file__, "temp_random_position")
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        plot_positions(positions, ax=ax)
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        assert os.path.exists(img)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
