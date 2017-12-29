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
from src.code_beatrix.faq.faq_video import extract_video, save_video, video_enumerate_frames


class TestVideo(ExtTestCase):

    def test_extract_avideo(self):
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

    def test_extract_frames(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        vid = os.path.join(os.path.dirname(__file__), 'data', 'videxa.mp4')
        fra = list(video_enumerate_frames(vid))
        self.assertEqual(len(fra), 78)
        self.assertEqual(fra[0].shape, (720, 404, 3))

    def test_extract_frames_img(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_extract_frames_img")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        fns = list(video_enumerate_frames(vid, folder=temp))
        self.assertEqual(len(fns), 78)


if __name__ == "__main__":
    unittest.main()
