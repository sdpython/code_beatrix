"""
@brief      test log(time=1s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from code_beatrix.ipythonhelper.magic_scratch import MagicScratch
from code_beatrix.jsscripts.nbsnap import RenderSnap


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
        self.assertTrue(res)

    def test_snap(self):
        obj = RenderSnap()
        s = obj._repr_html_()
        self.assertTrue(s)


if __name__ == "__main__":
    unittest.main()
