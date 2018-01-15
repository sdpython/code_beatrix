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
from src.code_beatrix.art.video import video_save, video_compose


class TestVideoPlacement(ExtTestCase):

    def test_modify_placement(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_placement")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')

        vid2 = video_compose(vid, vid, t2=1, place='h2')
        exp = os.path.join(temp, "h2.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)

        vid2 = video_compose(vid, vid, t2=1, place='v2')
        exp = os.path.join(temp, "v2.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)

        vid2 = video_compose(vid, vid, t2=1, place='br', zoom=0.2)
        exp = os.path.join(temp, "br.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
