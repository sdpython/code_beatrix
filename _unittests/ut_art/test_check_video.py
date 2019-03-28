"""
@brief      test log(time=0s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from code_beatrix import check


class TestCheckVideo(unittest.TestCase):

    def test_check(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        check(kind="video", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
