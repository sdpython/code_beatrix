"""
@brief      test log(time=0s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pytube.exceptions import RegexMatchError  # pylint: disable=C0411
from code_beatrix import check


class TestCheckVideo(unittest.TestCase):

    def test_check(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            check(kind="video", fLOG=fLOG)
        except RegexMatchError as e:
            if "zero match" not in str(e):
                raise e
            warnings.warn("pytube issue: {}".format(e))


if __name__ == "__main__":
    unittest.main()
