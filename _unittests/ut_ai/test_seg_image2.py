# -*- coding: utf-8 -*-
"""
@brief      test log(time=14s)
"""
import os
import unittest
import warnings
import skimage
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase


class TestSegImage2(ExtTestCase):

    def test_seg_image2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_seg_image2")
        img1 = os.path.join(temp, "..", "data", "Mona_elephant.jpg")
        imgs = [img1]

        from code_beatrix.ai import DLImageSegmentation
        try:
            dl = DLImageSegmentation(fLOG=fLOG)
        except FileNotFoundError as e:
            warnings.warn(str(e))
            return

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
