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

from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv
from src.code_beatrix.algorithm.data import load_prenoms_w
from src.code_beatrix.algorithm.classroom import random_positions, plot_positions, optimize_positions, find_best_positions_greedy, measure_positions


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
        assert ax is not None
        clog("savefig")
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        assert os.path.exists(img)
        clog("noshow")
        if __name__ == "__main__":
            fig.show()
        clog("close")
        plt.close('all')
        clog("end")
        fLOG("end")

    def test_find_greedy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        positions = [('Warren', 0, 0), ('Wallerand', 0, 1), ('Walfroy', 0, 2), ('Walfrid', 0, 3),
                     ('Waldy', 0, 4), ('Weltaz', 1,
                                       0), ('Wendy', 1, 1), ('Wilbrord', 1, 2),
                     ('Werburge', 1, 3), ('Wandy', 1,
                                          4), ('Walburge', 2, 0), ('Walder', 2, 1),
                     ('Wafaa', 2, 2), ('Waldemar', 2,
                                       3), ('Waudru', 2, 4), ('Walter', 3, 0),
                     ('Wilfrid', 3, 1), ('Werner', 3,
                                         2), ('Wandrille', 3, 3), ('Walther', 3, 4),
                     ('Wilbert', 4, 0), ('Wenceslas', 4, 1), ('Waast', 4, 2), ('Wanda', 4, 3)]
        names = list(name for name, x, y in positions)
        names.sort()
        edges = [(names[0], names[1]), (names[0], names[2]), (names[0], names[3]),
                 (names[3], names[4]), (names[3], names[5]), (names[0], names[6])]
        edges_dict = {}
        for name1, name2 in edges:
            if name1 in edges_dict:
                edges_dict[name1].append(name2)
            else:
                edges_dict[name1] = [name2]
            if name2 in edges_dict:
                edges_dict[name2].append(name1)
            else:
                edges_dict[name2] = [name1]

        positions = {k: (x, y) for k, x, y in positions}
        edges_dict = {k: set(v) for k, v in edges_dict.items()}

        res = find_best_positions_greedy(positions, edges_dict, names[0])
        d0 = measure_positions(positions, edges)
        d0_ = measure_positions(positions, edges_dict)
        assert abs(d0 - d0_) < 1e-5
        delta, pos = res[0]

        rev = {v: k for k, v in positions.items()}
        current_name = rev[pos]

        c = positions.copy()
        p0 = positions[names[0]]
        p = positions[current_name]
        positions[current_name] = p0
        positions[names[0]] = p

        d1 = measure_positions(positions, edges)
        fLOG("d1", d1)
        assert c != positions
        assert abs(d1 - d0 - delta) < 1e-5

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
            assert ax is not None
            img = os.path.join(temp, "img.png")
            fig.savefig(img)
            assert os.path.exists(img)
            if __name__ == "__main__":
                fig.show()
            plt.close('all')
            fLOG("end")
        else:
            new_positions, iter = optimize_positions(
                positions, edges, fLOG=fLOG, max_iter=20)
            for i in iter:
                fLOG(i)
            assert iter
            assert new_positions


if __name__ == "__main__":
    unittest.main()
