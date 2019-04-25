# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""
import os
import unittest
import warnings
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, skipif_circleci
from pytube.exceptions import RegexMatchError
from code_beatrix.art.video import download_youtube_video



class TestVideoDownload(ExtTestCase):

    @skipif_circleci("unexpected error: KeyError: 'url_encoded_fmt_stream_map'")
    def test_video_download(self):
        temp = get_temp_folder(__file__, "temp_video_download")
        try:
            download_youtube_video('vHcfbOqYztU', output_path=temp)
        except RegexMatchError as e:
            warnings.warn("Issue with video '{}' - {}".format('vHcfbOqYztU', e))
            return
        exp = os.path.join(temp, "vidéo tres courte.mp4")
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
