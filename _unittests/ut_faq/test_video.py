# -*- coding: utf-8 -*-
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
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from src.code_beatrix.faq.faq_video import extract_video, save_video


class TestVideo(ExtTestCase):

    def test_extract_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_extract")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        fLOG('extract')
        vid2 = extract_video(vid, '00:00:01', '00:00:04')
        fLOG('save')
        exp = os.path.join(temp, "courte.mp4")
        save_video(vid2, exp)
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
