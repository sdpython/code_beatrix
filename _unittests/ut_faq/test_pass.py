"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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


from src.code_beatrix.faq.faq_python import instruction_pass


class TestPass(unittest.TestCase):

    def test_pass(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        instruction_pass()


if __name__ == "__main__":
    unittest.main()
