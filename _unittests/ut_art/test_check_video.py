"""
@brief      test log(time=0s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pytube.exceptions import RegexMatchError  # pylint: disable=C0411
from code_beatrix import check


class TestCheckVideo(unittest.TestCase):

    def test_check_youtube(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            check(kind="video", fLOG=fLOG)
        except RegexMatchError as e:
            import pytube
            if "zero match" not in str(e):
                raise e
            warnings.warn("RegexMatchError: pytube version {} - pytube issue: {}".format(
                pytube.__version__, e))
        except KeyError as e:
            import pytube
            warnings.warn("KeyError: pytube version {} - pytube issue: {}".format(
                pytube.__version__, e))


if __name__ == "__main__":
    unittest.main()
