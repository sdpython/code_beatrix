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
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from code_beatrix.art.video import video_save, video_frame, clean_video


class TestVideoImage(ExtTestCase):

    def test_video_frame(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        import gizeh
        temp = get_temp_folder(__file__, "temp_video_frame")

        def make_frame(t):
            # See example: https://zulko.github.io/moviepy/getting_started/videoclips.html#videoclip
            surface = gizeh.Surface(128, 128)
            radius = 100 * (1 + (t * (2 - t))**2) / 6
            circle = gizeh.circle(radius, xy=(64, 64), fill=(1, 0, 0))
            circle.draw(surface)
            return surface.get_npimage()

        vid = video_frame(make_frame)
        exp = os.path.join(temp, "courte.gif")
        video_save(vid, exp, fps=20, duration=2)
        self.assertExists(exp)
        clean_video(vid)

    def test_video_frame_sequence(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_frame_images")
        fold = os.path.join(temp, "..", "data", "images")
        vid = video_frame(fold, fps=4)
        exp = os.path.join(temp, "courte.gif")
        video_save(vid, exp)
        self.assertExists(exp)
        clean_video(vid)


if __name__ == "__main__":
    unittest.main()
