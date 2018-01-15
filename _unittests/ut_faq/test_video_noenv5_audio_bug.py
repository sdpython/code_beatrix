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
from src.code_beatrix.faq.faq_video import video_save, video_modification, video_replace_audio, video_extract_audio, video_concatenate, audio_concatenate


class TestVideoAudioBug(ExtTestCase):

    def test_video_audio_bug(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_audio_bug")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        audio = video_extract_audio(vid)
        vid2 = video_modification(vid, speed=2., mirrory=True, mirrorx=True)
        audio1 = video_extract_audio(vid2)
        audio3 = audio_concatenate([audio1, audio, audio1, audio1])
        vid3 = video_concatenate([vid, vid2])
        vid4 = video_replace_audio(vid3, audio3)
        exp = os.path.join(temp, "courte2x.mp4")
        video_save(vid4, exp)
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
