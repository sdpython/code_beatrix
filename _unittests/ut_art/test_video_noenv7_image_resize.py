# -*- coding: utf-8 -*-
"""
@brief      test log(time=1001s)

Duration is around a few seconds but the test needs to be run
at the end of the series of unitests as it interferes
with the notebook unittesting (it uses Popen too).
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from code_beatrix.art.video import video_save, video_image, video_resize, clean_video


class TestVideoImageResize(ExtTestCase):

    def test_video_image_resize(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_resize")
        nimg = os.path.join(temp, '..', 'data', 'GastonLagaffe_1121.jpg')
        vid = video_image(nimg, duration=60, zoom=(200, 200))
        exp = os.path.join(temp, "courte.mp4")
        video_save(vid, exp, fps=20)
        self.assertExists(exp)
        clean_video(vid)

        exp = os.path.join(temp, "courtecb.mp4")
        img = video_image(nimg, duration=60, zoom=(200, 200))
        vid = video_resize(img, 0.5)
        video_save(vid, exp, fps=20)
        self.assertExists(exp)
        clean_video([vid, img])

        exp = os.path.join(temp, "courtefct.mp4")
        img = video_image(nimg, duration=60, zoom=(200, 200))
        vid = video_resize(img, lambda t: max(0.1, 1 - 0.1 * t))
        video_save(vid, exp, fps=20)
        self.assertExists(exp)
        clean_video([vid, img])


if __name__ == "__main__":
    unittest.main()
