#-*- coding: utf-8 -*-
"""
@brief      test log(time=4s)
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

from pyquickhelper import fLOG, get_temp_folder
from src.code_beatrix.algorithm import voyageur_commerce_simple, distance_circuit, plot_circuit


class TestTsp (unittest.TestCase):

    def test_voyageur_commerce_simple(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        points = [(105.61666870117188, 69.01666259765625),
                  (192.61666870117188, 92.01666259765625),
                  (372.6166687011719, 123.01666259765625),
                  (360.6166687011719, 249.01666259765625),
                  (190.61666870117188, 213.01666259765625),
                  (102.61666870117188, 166.01666259765625),
                  (104.61666870117188, 271.01666259765625),
                  (209.61666870117188, 278.01666259765625),
                  (321.6166687011719, 198.01666259765625),
                  (261.6166687011719, 153.01666259765625),
                  (196.61666870117188, 162.01666259765625),
                  (317.6166687011719, 306.01666259765625)]

        d0 = distance_circuit(points)

        newp = voyageur_commerce_simple(points)

        d1 = distance_circuit(newp)

        fLOG(d0, d1)
        assert d1 < d0

        if __name__ == "__main__":
            import matplotlib.pyplot as plt
            ax = plot_circuit(newp)
            plt.show()

if __name__ == "__main__":
    unittest.main()