"""
@brief      test log(time=0s)
"""
import unittest
import warnings
from pyquickhelper.pycode import skipif_travis, ExtTestCase
from code_beatrix.jsscripts import copy_jstool2notebook


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
