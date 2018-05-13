# -*- coding: utf-8 -*-
"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv


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


from src.code_beatrix.algorithm.classroom import random_positions, plot_positions, optimize_positions


class TestClassRoom36(unittest.TestCase):

    def test_optimize_position(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        positions = random_positions(24)
        names = list(name for name, x, y in positions)
        names.sort()
        edges = [(names[0], names[1]), (names[0], names[2]), (names[0], names[3]),
                 (names[3], names[4]), (names[3], names[5]), (names[0], names[6])]

        if __name__ == "__main__":
            temp = get_temp_folder(__file__, "temp_optimization")
            new_positions, iter = optimize_positions(
                positions, edges, fLOG=fLOG, max_iter=20, plot_folder=temp)
            for i in iter:
                fLOG(i)
            positions = [(k, ) + v for k, v in new_positions.items()]
            fix_tkinter_issues_virtualenv()
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
            plot_positions(positions, edges=edges, ax=ax)
            self.assertTrue(ax is not None)
            img = os.path.join(temp, "img.png")
            fig.savefig(img)
            self.assertTrue(os.path.exists(img))
            if __name__ == "__main__":
                fig.show()
            plt.close('all')
            fLOG("end")
        else:
            new_positions, iter = optimize_positions(
                positions, edges, fLOG=fLOG, max_iter=20)
            for i in iter:
                fLOG(i)
            self.assertTrue(iter is not None)
            self.assertTrue(new_positions is not None)


if __name__ == "__main__":
    unittest.main()
