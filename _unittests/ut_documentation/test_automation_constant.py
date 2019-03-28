"""
@brief      test log(time=4s)
@author     Xavier Dupre
"""
import unittest
from pyquickhelper.loghelper import fLOG
from code_beatrix.automation.notebook_const_helper import voyageur_de_commerce_points


class TestAutomationConstant(unittest.TestCase):

    def test_constant(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        voyageur_de_commerce_points()


if __name__ == "__main__":
    unittest.main()
