"""
@brief      test log(time=1s)
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


from pyquickhelper.loghelper import fLOG
from src.code_beatrix.ipythonhelper.magic_scratch import MagicScratch


class TestMagicSnap(unittest.TestCase):

    def test_magic_snap(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            # the module returns the following error
            # ENCODING ERROR WITH Python 2.7, will not fix it
            return
        else:
            password = "unittest" * 2

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
