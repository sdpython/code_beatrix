"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings


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
from src.code_beatrix.scratchs import check


class TestCheckScratchFiles(unittest.TestCase):

    def test_check(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        check()


if __name__ == "__main__":
    unittest.main()
