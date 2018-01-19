"""
@file
@brief Draws objects on videos.
"""
import numpy
from cv2 import blur as cv_blur, rectangle as cv_rectangle
from cv2 import LINE_AA


def blur(img, p1, p2, kernel_size=(5, 5)):
    """
    Blurs a part of a picture.
    Uses `blur <https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=blur#blur>`_.

    @param      img         image (:epkg:`numpy:array`)
    @param      p1          (x1,y1)
    @param      p2          (x2, y2)
    @param      kernel_size kernel size for the bluring.

    It modifies the original picture.
    """
    h, w, d = img.shape
    x1, y1 = p1
    x2, y2 = p2
    x1, x2 = max(0, x1), min(x2, w)
    y1, y2 = max(0, y1), min(y2, h)
    dx, dy = x2 - x1, y2 - y1

    region_size = dy, dx
    r_blur = max(min(region_size) * 2 // 3, 5)
    mask = numpy.zeros(region_size).astype('uint8')
    cv_rectangle(mask, (y1, x1), (y2, x2), 255, -1, lineType=LINE_AA)
    mask = numpy.dstack(3 * [(1.0 / 255) * mask])
    orig = img[y1:y2, x1:x2]
    zone = cv_blur(orig, (r_blur, r_blur))
    img[y1:y2, x1:x2] = mask * zone + (1 - mask) * orig


def rectangle(img, p1, p2, color=(255, 255, 0)):
    """
    Draws a rectangle.
    Uses `blur <https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=blur#blur>`_.

    @param      img         image (:epkg:`numpy:array`)
    @param      p1          (x1,y1)
    @param      p2          (x2, y2)
    @param      kernel_size kernel size for the bluring.

    It modifies the original picture.
    """
    h, w, d = img.shape
    x1, y1 = p1
    x2, y2 = p2
    x1, x2 = max(0, x1), min(x2, w)
    y1, y2 = max(0, y1), min(y2, h)
    cv_rectangle(img, (x1, y1), (x2, y2), color)
