# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""
import os
import unittest
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, skipif_circleci
from code_beatrix.art.video import download_youtube_video


class TestVideoDownload(ExtTestCase):

    @skipif_circleci("unexpected error: KeyError: 'url_encoded_fmt_stream_map'")
    def test_video_download(self):
        temp = get_temp_folder(__file__, "temp_video_download")
        download_youtube_video('vHcfbOqYztU', output_path=temp)
        exp = os.path.join(temp, "vidéo tres courte.mp4")
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
