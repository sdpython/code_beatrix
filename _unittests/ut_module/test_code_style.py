"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase

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


class TestCodeStyle(ExtTestCase):
    """Test style."""

    def test_src(self):
        "skip pylint"
        self.assertFalse(src is None)

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0212', 'W0622', 'W0703', 'W0201',
                                  'W0221', 'W0223'),
                   skip=["No name 'rectangle' in module 'cv2'",
                         "No name 'blur' in module 'cv2'",
                         "No name 'CascadeClassifier' in module 'cv2'",
                         "No name 'CASCADE_SCALE_IMAGE' in module 'cv2'",
                         "Module 'moviepy.video.fx.all' has no '",
                         "Module 'chainer.cuda' has no '",
                         "Module 'chainer.cuda' has no ",
                         "Module 'moviepy.audio.fx.all' has no ",
                         "image_segmentation.py:77: R1710",
                         ])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0212', 'W0622'),
                   skip=["src' imported but unused",
                         "skip_' imported but unused",
                         "skip__' imported but unused",
                         "skip___' imported but unused",
                         "Unused variable 'skip_'",
                         "Unused variable 'skip_",
                         "imported as skip_",
                         "Unused import src",
                         ])


if __name__ == "__main__":
    unittest.main()