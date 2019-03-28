# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)

Duraction is around a few seconds but the test needs to be run
at the end of the series of unitests as it interferes
with the notebook unittesting (it uses Popen too).
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from code_beatrix.art.video import video_save, video_text, video_position, video_compose, video_image, clean_video


class TestVideoTextImage(ExtTestCase):

    def test_video_text_image(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_video_text_image")
        img = os.path.join(temp, '..', 'data', 'GastonLagaffe_1121.jpg')
        vidimg0 = video_image(img, duration=5, opacity=200)
        vidimg = video_position(vidimg0, lambda t: (0, 0), relative=True)

        text0 = video_text('boule', size=2., color=(
            255, 0, 0, 128), background=(0, 255, 0, 100))
        text = video_position(text0, lambda t: (
            t * 0.1, t * 0.2), relative=True)

        comb = video_compose([vidimg, text], t1=[0, 1])
        exp1 = os.path.join(temp, "courte_text.mp4")
        exp2 = os.path.join(temp, "courte_laga.mp4")
        video_save(text, exp1, fps=20, duration=5,
                   verbose=__name__ == "__main__")
        video_save(comb, exp2, fps=20, duration=5,
                   verbose=__name__ == "__main__")
        self.assertExists(exp1)
        self.assertExists(exp2)
        clean_video([text, text0, comb, vidimg, vidimg0])


if __name__ == "__main__":
    unittest.main()
