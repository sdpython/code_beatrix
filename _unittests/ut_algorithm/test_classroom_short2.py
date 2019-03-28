# -*- coding: utf-8 -*-
"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from code_beatrix.algorithm.data import load_prenoms_w


class TestClassRoomShort2(unittest.TestCase):

    def test_names(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        names = load_prenoms_w()
        self.assertEqual(len(names), 50)


if __name__ == "__main__":
    unittest.main()
