"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.pycode import skipif_travis, ExtTestCase


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


class TestCopyTools(ExtTestCase):

    @skipif_travis("travis, unable to test TestCopyTools.test_copy_tools")
    def test_copy_tools(self):
        try:
            res = copy_jstool2notebook("snap")
        except PermissionError as e:
            warnings.warn(
                "Cannot copy, user has no permission to modify python distribution {0}".format(e))
            return
        if res is not None:
            self.assertIsInstance(res, list)


if __name__ == "__main__":
    unittest.main()
