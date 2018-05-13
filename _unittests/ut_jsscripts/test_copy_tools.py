"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings
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


from src.code_beatrix.jsscripts import copy_jstool2notebook


class TestCopyTools(unittest.TestCase):

    def test_copy_tools(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            warnings.warn(
                "travis, unable to test TestCopyTools.test_copy_tools")
            return

        res = copy_jstool2notebook("snap")
        assert isinstance(res, list)


if __name__ == "__main__":
    unittest.main()
