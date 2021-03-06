# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)

Duration is around a few seconds but the test needs to be run
at the end of the series of unitests as it interferes
with the notebook unittesting (it uses Popen too).
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from code_beatrix.art.video import video_enumerate_frames, video_load, clean_video


class TestVideoOpenProcess(ExtTestCase):

    def test_extract_frames_check_open(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        vid = video_load(os.path.join(
            os.path.dirname(__file__), 'data', 'videxa.mp4'))
        fra = list(video_enumerate_frames(vid, clean=True))
        self.assertEqual(len(fra), 78)
        self.assertEqual(fra[0].shape, (720, 404, 3))
        clean_video(vid)


if __name__ == "__main__":
    unittest.main()
