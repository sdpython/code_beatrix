# -*- coding: utf-8 -*-
"""
@brief      test log(time=14s)
"""

import sys
import os
import unittest
import skimage
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


from src.code_beatrix.ai import DLImageSegmentation


class TestSegImage2(ExtTestCase):

    def test_seg_image2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_seg_image2")
        img1 = os.path.join(temp, "..", "data", "Mona_elephant.jpg")
        imgs = [img1]

        dl = DLImageSegmentation(fLOG=fLOG)

        for i, img in enumerate(imgs):
            feat, res = dl.predict(img, resize=('max2', 200))
            viz = dl.plot(feat, res)

            out_file = os.path.join(temp, "out_img%d.png" % i)
            skimage.io.imsave(out_file, viz)
            self.assertExists(out_file)

        if __name__ == "__main__":
            skimage.io.imshow(viz)
            skimage.io.show()


if __name__ == "__main__":
    unittest.main()