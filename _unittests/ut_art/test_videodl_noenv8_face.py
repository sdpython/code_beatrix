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
from src.code_beatrix.art.videodl import video_map_images
from src.code_beatrix.art.video import video_save, video_extract_video, video_save_image


class TestVideoDLFace(ExtTestCase):

    def _test_modify_avideo_blur(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_videodl_face_blur")
        vid = os.path.join(temp, '..', 'data', 'mary.mp4')
        vide = video_extract_video(vid, 0, 5 if __name__ == "__main__" else 1)
        vid2 = video_map_images(
            vide, fps=10, name="detect", progress_bar=__name__ == "__main__", fLOG=fLOG)
        exp = os.path.join(temp, "face.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)
        vid2.cbclean()

    def test_modify_avideo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_videodl_face_rect")
        vid = os.path.join(temp, '..', 'data', 'charlie.mp4')
        vide = video_extract_video(vid, 0, 5 if __name__ == "__main__" else 1)
        vid2 = video_map_images(
            vide, fps=10, name="detect", action="rect", progress_bar=__name__ == "__main__", fLOG=fLOG)
        exp = os.path.join(temp, "face.mp4")
        self.assertTrue(vid2.make_frame is not None)
        video_save_image(vid2, t=1, filename=os.path.join(temp, "img1.jpg"))
        im = video_save_image(vid2, t=2)
        im.save(os.path.join(temp, "img2.png"))
        video_save(vid2, exp, verbose=__name__ == "__main__")
        self.assertExists(exp)
        # vid2.cbclean()


if __name__ == "__main__":
    unittest.main()
