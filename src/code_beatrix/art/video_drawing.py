"""
@file
@brief Draws objects on videos.
"""
from cv2 import blur as cv_blur, rectangle as cv_rectangle


def blur(img, p1, p2, frac=0.333, kernel_size=None):
    """
    Blurs a part of a picture.
    Uses `blur <https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=blur#blur>`_.

    @param      img         image (:epkg:`numpy:array`)
    @param      p1          (x1,y1)
    @param      p2          (x2, y2)
    @param      frac        if not None, if *kernel_size* is equal to this fraction
                            of the original frame
    @param      kernel_size kernel size for the bluring (wins over *frac*)

    It modifies the original picture.
    """
    h, w, d = img.shape
    x1, y1 = p1
    x2, y2 = p2
    x1, x2 = max(0, x1), min(x2, w)
    y1, y2 = max(0, y1), min(y2, h)
    dx, dy = x2 - x1, y2 - y1

    if kernel_size is not None:
        blur_size = kernel_size
    else:
        blur_size = (int(frac * dx), int(frac * dy))
    orig = img[y1:y2, x1:x2]
    zone = cv_blur(orig, blur_size)
    img[y1:y2, x1:x2] = zone


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
