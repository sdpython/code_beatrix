# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv
from code_beatrix.algorithm.classroom import random_positions, plot_positions


class TestClassRoomShort1(unittest.TestCase):

    def test_random_position(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_random_position")
        clog = CustomLog(temp)
        clog("random_positions")
        fLOG("random_positions")
        positions = random_positions(24)
        self.assertEqual(len(positions), 24)

        clog("beginning")
        fLOG("beginning")
        fix_tkinter_issues_virtualenv()
        clog("fix")
        fLOG("fix")
        import matplotlib.pyplot as plt
        clog("plotting")
        fLOG("plotting")
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        clog("plotting positions")
        fLOG("plotting positions")
        plot_positions(positions, ax=ax)
        self.assertTrue(ax is not None)
        clog("savefig")
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        self.assertTrue(os.path.exists(img))
        clog("noshow")
        if __name__ == "__main__":
            fig.show()
        clog("close")
        plt.close('all')
        clog("end")
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
