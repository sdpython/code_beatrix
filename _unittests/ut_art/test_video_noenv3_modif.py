# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)
"""


import sys
import os
import unittest
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


from src.code_beatrix.art.video import video_save, video_modification, clean_video, video_load


class TestVideoModif(ExtTestCase):

    def test_modify_avideo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_modification")
        vid = video_load(os.path.join(temp, '..', 'data', 'videxa.mp4'))
        vid2 = video_modification(vid, speed=2., mirrory=True, mirrorx=True)
        exp = os.path.join(temp, "courte2x.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)
        clean_video([vid2, vid])


if __name__ == "__main__":
    unittest.main()
