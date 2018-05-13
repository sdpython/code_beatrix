# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)

Duration is around a few seconds but the test needs to be run
at the end of the series of unitests as it interferes
with the notebook unittesting (it uses Popen too).
This is true for similar unit tests.
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


from src.code_beatrix.art.video import audio_compose, audio_save, audio_extract_audio, audio_concatenate


class TestAudio(ExtTestCase):

    def test_compose_audio(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_audio_compose")
        aud = os.path.join(temp, '..', 'data', 'cartoon011.wav')

        aud2 = audio_compose(aud, aud, 1, 3)
        exp = os.path.join(temp, "courte_audio.wav")
        audio_save(aud2, exp)
        self.assertExists(exp)

        aud3 = audio_concatenate([aud, aud])
        exp = os.path.join(temp, "courte_audio2.wav")
        audio_save(aud3, exp)
        self.assertExists(exp)

    def test_extract_audio(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_audio_extract")
        aud = os.path.join(temp, '..', 'data', 'cartoon026.wav')

        aud2 = audio_extract_audio(aud, '00:00:01', '00:00:02')
        exp = os.path.join(temp, "courte_audio.wav")
        audio_save(aud2, exp)
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
