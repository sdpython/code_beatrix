# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)
"""


import sys
import os
import unittest
import subprocess
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase


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


from src.code_beatrix.art.video import video_enumerate_frames


class TestLONGVideo(ExtTestCase):

    def test_extract_frames_img(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_extract_frames_img")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        fns = list(video_enumerate_frames(vid, folder=temp, clean=True))
        self.assertEqual(len(fns), 78)
        subprocess._cleanup()


if __name__ == "__main__":
    unittest.main()
