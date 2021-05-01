# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)

Duration is around a few seconds but the test needs to be run
at the end of the series of unitests as it interferes
with the notebook unittesting (it uses Popen too).
"""
import os
import unittest
import warnings
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, skipif_circleci
from code_beatrix.art.videodl import video_map_images
from code_beatrix.art.video import video_save, video_extract_video, clean_video, video_load


class TestVideoDLPeople(ExtTestCase):

    @skipif_circleci("Received 'killed' signal")
    def test_modify_avideo(self):
        temp = get_temp_folder(__file__, "temp_videodl_people")
        vid = video_load(os.path.join(temp, '..', 'data', 'mur.mp4'))
        vide = video_extract_video(vid, 0, 5 if __name__ == "__main__" else 1)
        try:
            vid2 = video_map_images(
                vide, fps=10, name="people",
                logger='bar' if __name__ == "__main__" else None)
        except FileNotFoundError as e:
            warnings.warn(str(e))
            return
        exp = os.path.join(temp, "people.mp4")
        video_save(vid2, exp)
        self.assertExists(exp)
        clean_video([vid2, vid, vide])


if __name__ == "__main__":
    unittest.main()
