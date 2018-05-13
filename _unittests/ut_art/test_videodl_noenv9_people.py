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
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, skipif_circleci


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


from src.code_beatrix.art.videodl import video_map_images
from src.code_beatrix.art.video import video_save, video_extract_video, clean_video, video_load


class TestVideoDLPeople(ExtTestCase):

    @skipif_circleci("Received 'killed' signal")
    def test_modify_avideo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_videodl_people")
        vid = video_load(os.path.join(temp, '..', 'data', 'mur.mp4'))
        vide = video_extract_video(vid, 0, 5 if __name__ == "__main__" else 1)
        vid2 = video_map_images(
            vide, fps=10, name="people", progress_bar=__name__ == "__main__", fLOG=fLOG)
        exp = os.path.join(temp, "people.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)
        clean_video([vid2, vid, vide])


if __name__ == "__main__":
    unittest.main()
