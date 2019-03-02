# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, is_travis_or_appveyor, skipif_circleci


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


from src.code_beatrix.art.video import download_youtube_video


class TestVideoDownload(ExtTestCase):

    @skipif_circleci("unexpected error: KeyError: 'url_encoded_fmt_stream_map'")
    def test_video_download(self):
        temp = get_temp_folder(__file__, "temp_video_download")
        download_youtube_video('vHcfbOqYztU', output_path=temp)
        exp = os.path.join(temp, "vidéo tres courte.mp4")
        self.assertExists(exp)


if __name__ == "__main__":
    unittest.main()
