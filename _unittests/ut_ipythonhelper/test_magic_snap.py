"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest


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


from pyquickhelper.loghelper import fLOG
from src.code_beatrix.ipythonhelper.magic_scratch import MagicScratch


class TestMagicSnap(unittest.TestCase):

    def test_magic_snap(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.abspath(__file__)
        mg = MagicScratch()
        cmd = "-W 500"
        fLOG("**", cmd)
        mg.add_context({"this": this})
        res = mg.snap(cmd)
        fLOG(res)
        assert res is not None


if __name__ == "__main__":
    unittest.main()
