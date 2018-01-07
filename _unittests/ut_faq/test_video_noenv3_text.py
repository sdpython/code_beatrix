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
from src.code_beatrix.faq.faq_video import video_save, video_text, video_position, video_compose, video_image


class TestVideoText(ExtTestCase):

    def test_video_text(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_text")
        vid = img = video_text('boule')
        exp = os.path.join(temp, "courte.mp4")
        video_save(vid, exp, fps=20, duration=3)
        self.assertExists(exp)

        exp = os.path.join(temp, "courtefct.mp4")
        vid = video_position(img, lambda t: (t * 0.1, t * 0.2), relative=True)
        video_save(vid, exp, fps=20, duration=4)
        self.assertExists(exp)

    def test_video_text_image(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_video_text_image")
        img = os.path.join(temp, '..', 'data', 'GastonLagaffe_1121.jpg')
        vidimg = video_image(img, duration=5, opacity=200)
        vidimg = video_position(vidimg, lambda t: (0, 0), relative=True)

        text = video_text('boule', size=2., color=(
            255, 0, 0, 128), background=(0, 255, 0, 100))
        text = video_position(text, lambda t: (
            t * 0.1, t * 0.2), relative=True)

        comb = video_compose([vidimg, text], t1=[0, 1])
        exp1 = os.path.join(temp, "courte_text.mp4")
        exp2 = os.path.join(temp, "courte_laga.mp4")
        video_save(text, exp1, fps=20, duration=5)
        video_save(comb, exp2, fps=20, duration=5)
        self.assertExists(exp1)
        self.assertExists(exp2)


if __name__ == "__main__":
    unittest.main()
