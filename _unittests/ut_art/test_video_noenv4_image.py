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
from src.code_beatrix.art.video import video_save, video_image, video_position, video_resize


class TestVideoImage(ExtTestCase):

    def test_video_image_position(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_position")
        img = os.path.join(temp, '..', 'data', 'GastonLagaffe_1121.jpg')
        vid = img = video_image(img, duration=60, zoom=(200, 200))
        exp = os.path.join(temp, "courte.mp4")
        video_save(vid, exp, fps=20)
        self.assertExists(exp)

        exp = os.path.join(temp, "courte05.mp4")
        vid = video_position(img, (0.5, 0.5), relative=True)
        video_save(vid, exp, fps=20)
        self.assertExists(exp)

        exp = os.path.join(temp, "courtecb.mp4")
        vid = video_position(img, ('center', 'bottom'), relative=True)
        video_save(vid, exp, fps=20)
        self.assertExists(exp)

        exp = os.path.join(temp, "courtefct.mp4")
        vid = video_position(img, lambda t: (t * 0.1, t * 0.2), relative=True)
        video_save(vid, exp, fps=20)
        self.assertExists(exp)

    def test_video_image_resize(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_resize")
        img = os.path.join(temp, '..', 'data', 'GastonLagaffe_1121.jpg')
        vid = img = video_image(img, duration=60, zoom=(200, 200))
        exp = os.path.join(temp, "courte.mp4")
        video_save(vid, exp, fps=20)
        self.assertExists(exp)

        exp = os.path.join(temp, "courtecb.mp4")
        vid = video_resize(img, 0.5)
        video_save(vid, exp, fps=20)
        self.assertExists(exp)

        exp = os.path.join(temp, "courtefct.mp4")
        vid = video_resize(img, lambda t: max(0.1, 1 - 0.1 * t))
        video_save(vid, exp, fps=20)
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
