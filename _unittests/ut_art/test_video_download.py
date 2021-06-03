# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""
import os
import unittest
import warnings
import urllib.error
from pyquickhelper.pycode import (
    get_temp_folder, ExtTestCase, skipif_circleci,
    skipif_appveyor, skipif_travis)
from pytube.exceptions import RegexMatchError, VideoUnavailable  # pylint: disable=C0411
from code_beatrix.art.video import download_youtube_video


class TestVideoDownload(ExtTestCase):

    @skipif_circleci("unexpected error: KeyError: 'url_encoded_fmt_stream_map'")
    @skipif_appveyor("connectivity issues")
    @skipif_travis("connectivity issues")
    def test_video_download(self):
        temp = get_temp_folder(__file__, "temp_video_download")
        try:
            download_youtube_video('vHcfbOqYztU', output_path=temp)
        except (RegexMatchError, RuntimeError) as e:
            if ("zero match" not in str(e) and "Unable to process tag" not in str(e)):
                raise e
            import pytube
            warnings.warn("RegexMatchError: pytube version {} - pytube issue: {}".format(
                pytube.__version__, e))
            return
        except VideoUnavailable as e:
            import pytube
            warnings.warn("VideoUnavailable: pytube version {} - pytube issue: {}".format(
                pytube.__version__, e))
            return
        except KeyError as e:
            import pytube
            warnings.warn("KeyError: pytube version {} - pytube issue: {}".format(
                pytube.__version__, e))
            return
        except urllib.error.HTTPError as e:
            warnings.warn("HTTP issue: {}".format(e))
            return
        exp = os.path.join(temp, "vidéo tres courte.mp4")
        if __name__ == "__main___":
            self.assertExists(exp)
        if not os.path.exists(exp):
            warnings.warn("Unable to find '{}'.".format(exp))


if __name__ == "__main__":
    unittest.main()
