# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)

Duraction is around a few seconds but the test needs to be run
at the end of the series of unitests as it interferes
with the notebook unittesting (it uses Popen too).
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
from src.code_beatrix.art.video import video_save, video_extract_video, video_compose, video_concatenate, clean_video


class TestVideo(ExtTestCase):

    def test_extract_avideo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_extract")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        vid2 = video_extract_video(vid, '00:00:01', '00:00:04')
        exp = os.path.join(temp, "courte.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)
        exp = os.path.join(temp, "courte.gif")
        video_save(vid2, exp)
        self.assertExists(exp)
        clean_video(vid2)

    def test_compose_avideo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_compose")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        vid2 = video_compose(vid, vid, '00:00:01', '00:00:04')
        exp = os.path.join(temp, "courte.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)

        exp = os.path.join(temp, "courte2.mp4")
        vid3 = video_concatenate([vid, vid])
        video_save(vid3, exp)
        self.assertExists(exp)
        clean_video(vid3)


if __name__ == "__main__":
    unittest.main()
