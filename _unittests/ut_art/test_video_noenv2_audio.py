# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase


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


from src.code_beatrix.art.video import video_save, video_replace_audio, video_extract_audio
from src.code_beatrix.art.video import video_remove_audio, audio_modification, audio_save, audio2wav


class TestAudioVideo(ExtTestCase):

    def test_extract_audio_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_video_audio")
        vid = os.path.join(temp, '..', 'data', 'videxa.mp4')
        aud = os.path.join(temp, '..', 'data', 'cartoon011.wav')
        vid = video_remove_audio(vid)
        audio2 = audio_modification(aud, volumex=5.5, fadein=True,
                                    speed=2., keep_duration=False,
                                    loop_duration=True)
        vid2 = video_replace_audio(vid, audio2, loop=False)
        self.assertTrue(video_extract_audio(vid2) is not None)
        exp = os.path.join(temp, "courte_audio.mp4")
        video_save(vid2, exp, verbose=__name__ == "__main__", duration=2)
        self.assertExists(exp)

        audio3 = audio2wav(audio2, duration=5, fps=44100)
        exp = os.path.join(temp, "courte_audio.mp3")
        audio_save(audio3, exp, verbose=__name__ == "__main__")
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
