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


class TestSegImage1(ExtTestCase):

    def test_seg_image1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_seg_image1")
        img1 = os.path.join(temp, "..", "data", "Mona_elephant.jpg")
        img2 = os.path.join(temp, "..", "data", "Tesla_circa_1890c.jpg")
        imgs = [img1, img2]

        from code_beatrix.ai import DLImageSegmentation
        try:
            dl = DLImageSegmentation(fLOG=fLOG)
        except FileNotFoundError as e:
            warnings.warn(str(e))
            return

        for i, img in enumerate(imgs):
            _, res = dl.predict(img)
            viz = dl.plot(img, res)

            out_file = os.path.join(temp, "out_img%d.png" % i)
            skimage.io.imsave(out_file, viz)
            self.assertExists(out_file)

        if __name__ == "__main__":
            skimage.io.imshow(viz)
            skimage.io.show()


if __name__ == "__main__":
    unittest.main()
