# -*- coding: utf-8 -*-
"""
@brief      test log(time=4s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from code_beatrix.algorithm.classroom import find_best_positions_greedy, measure_positions


class TestClassRoom(unittest.TestCase):

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
        self.assertTrue(abs(d0 - d0_) < 1e-5)
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
        self.assertTrue(c != positions)
        self.assertTrue(abs(d1 - d0 - delta) < 1e-5)


if __name__ == "__main__":
    unittest.main()
