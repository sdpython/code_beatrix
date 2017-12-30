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
from src.code_beatrix.faq.faq_video import video_save, video_replace_sound, video_extract_audio


class TestAudioVideo(ExtTestCase):

    def test_extract_audio_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_audio")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        aud = os.path.join(temp, '..', 'data', 'cartoon011.wav')
        vid2 = video_replace_sound(vid, aud, loop=True, volumex=5.5, fadein=True,
                                   t_end='00:00:05', speed=2.)
        self.assertTrue(video_extract_audio(vid2) is not None)
        exp = os.path.join(temp, "courte_audio.mp4")
        video_save(vid2, exp, verbose=False)
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
