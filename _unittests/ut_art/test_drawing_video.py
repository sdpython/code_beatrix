# -*- coding: utf-8 -*-
"""
@brief      test log(time=1000s)
"""
import os
import unittest
from skimage.io._plugins.pil_plugin import pil_to_ndarray
from PIL import Image
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from code_beatrix.art.video_drawing import rectangle, blur


class TestVideoDrawing(ExtTestCase):

    def test_rectangle(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_rectangle")
        img = os.path.join(temp, '..', 'data', 'img1.jpg')

        pil_img = Image.open(img)
        skimg = pil_to_ndarray(pil_img)
        im1 = skimg.copy().ravel()
        rectangle(skimg, (10, 20), (100, 200))
        im2 = skimg.copy().ravel()
        self.assertTrue(im1.tolist() != im2.tolist())
        pil_img2 = Image.fromarray(skimg)
        dest = os.path.join(temp, "img_rect.jpg")
        pil_img2.save(dest)

    def test_blur(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_blur")
        img = os.path.join(temp, '..', 'data', 'img1.jpg')

        pil_img = Image.open(img)
        skimg = pil_to_ndarray(pil_img)
        im1 = skimg.copy().ravel()
        blur(skimg, (10, 20), (100, 200))
        im2 = skimg.copy().ravel()
        self.assertTrue(im1.tolist() != im2.tolist())
        pil_img2 = Image.fromarray(skimg)
        dest = os.path.join(temp, "img_blur.jpg")
        pil_img2.save(dest)


if __name__ == "__main__":
    unittest.main()
