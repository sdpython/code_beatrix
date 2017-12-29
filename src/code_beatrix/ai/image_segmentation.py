"""
@file
@brief Extracts objects from an image based on deep learning.
"""
from contextlib import redirect_stdout
import io
import os
import chainer
import fcn
import skimage
import numpy
from PIL import Image
from skimage.io._plugins.pil_plugin import pil_to_ndarray
from .dlbase import DeepLearningImage


class DLImageSegmentation(DeepLearningImage):
    """
    Segments an image.
    Inspired from
    `infer.py <https://github.com/wkentaro/fcn/blob/master/examples/voc/infer.py>`_.
    See notebook :ref:`imagesegmentationrst`.
    """

    def __init__(self, model="FCN8s", n_class=21, gpu=False, class_name=None, fLOG=None):
        """
        @param      model       model name
        @param      n_class     number of classes
        @param      gpu         use gpu
        @param      class_name  class names
        @param      fLOG        logging function

        List of known models:

        * ``'FCN8s'``: image segmentation
        """
        self._fLOG = fLOG
        if model == "FCN8s":
            self.log(
                "[DLImageSegmentation] download model '{0}'".format(model))
            f = io.StringIO()
            with redirect_stdout(f):
                model_file = fcn.models.FCN8s.download()
            self.log('[DLImageSegmentation] {0}'.format(f.getvalue()))
            self._model_file = model_file
            model_class = fcn.models.FCN8s
            model = model_class(n_class=n_class)
            self.log("[DLImageSegmentation] load_npz '{0}'".format(model_file))
            chainer.serializers.load_npz(model_file, model)
        else:
            raise NotImplementedError(
                "Unable to interpret '{0}'".format(model))

        DeepLearningImage.__init__(self, model, gpu=gpu, fLOG=fLOG)
        self._n_class = n_class
        if class_name is None:
            self._class_name = class_name = fcn.datasets.VOC2012ClassSeg.class_names
        else:
            self._class_name = class_name
        self.log("[DLImageSegmentation] class_name '{0}'".format(class_name))

        if gpu:
            self.log("[DLImageSegmentation] gpu")
            chainer.cuda.get_device(self._gpu).use()
            model.to_gpu()
        else:
            self.log("[DLImageSegmentation] cpu")

    @property
    def ModelFile(self):
        """
        Returns the model file name.
        """
        return self._model_file

    def _new_size(self, old_size, new_size):
        """
        Computes a new size.

        @param      old_size        current size
        @param      new_size        new desired size
        @return                     new size

        *new_size* can be of:

        * (int, int): this is the new size
        * ('max2', int): this size is divided by 2 until the greater dimension
          is below a threshold
        """
        if not isinstance(new_size, tuple):
            raise TypeError("new_size must be a tuple")
        if not isinstance(old_size, tuple):
            raise TypeError("old_size must be a tuple")
        if len(old_size) != 2:
            raise ValueError("old_size must have two values")
        if len(new_size) != 2:
            raise ValueError("new_size must have two values")
        if isinstance(new_size[0], str):
            if new_size[0] == 'max2':
                mx = max(old_size)
                p = 1
                while mx > new_size[1]:
                    mx //= 2
                    p *= 2
                return (old_size[0] // p, old_size[1] // p)
            else:
                raise ValueError(
                    "Unable to interpret '{0}'".format(new_size[0]))
        elif isinstance(new_size[0], int):
            return new_size
        else:
            raise TypeError("new_size[0] must be an int")

    def _load_image(self, img, resize=None):
        """
        Loads an image as a :epkg:`numpy:array`.

        @param      img         image
        @param      resize      resize the image before predicting,
                                see @see me _new_size
        @return                 :epkg:`numpy:array`
        """
        if isinstance(img, str):
            # Loads the image.
            if not os.path.exists(img):
                raise FileNotFoundError(img)
            if resize is None:
                feat = skimage.io.imread(img)
            else:
                pilimg = Image.open(img)
                si = self._new_size(pilimg.size, resize)
                pilimg2 = pilimg.resize(si)
                feat = pil_to_ndarray(pilimg2)
        elif isinstance(img, numpy.ndarray):
            if resize is not None:
                raise NotImplementedError('resize not None is not implemented')
            feat = img
        else:
            raise NotImplementedError(
                "Not implemented for type '{0}'".format(type(img)))
        return feat

    def _preprocess(self, feat, preprocess=True):
        """
        Preprocesses the image before prediction.

        @param      feat        image (output of @see me _load_image)
        @param      preprocess  applies some preprocessing or not
        @return                 preprocessed image
        """
        if preprocess:
            input, = fcn.datasets.transform_lsvrc2012_vgg16((feat,))
            input = input[numpy.newaxis, :, :, :]
            return input
        else:
            return feat

    def predict(self, img, resize=None):
        """
        Applies the model on features *X*.

        @param      img     image
        @param      resize  resize the image before predicting,
                            see @see me _new_size
        @return             (image, prediction)
        """
        feat = self._load_image(img, resize=resize)
        input = self._preprocess(feat, preprocess=True)
        if self._gpu:
            input = chainer.cuda.to_gpu(input)

        with chainer.no_backprop_mode():
            input = chainer.Variable(input)
            with chainer.using_config('train', False):
                self._model(input)
                lbl_pred = chainer.functions.argmax(
                    self._model.score, axis=1)[0]
                lbl_pred = chainer.cuda.to_cpu(lbl_pred.data)

        return feat, lbl_pred

    def plot(self, img, pred):
        """
        Displays the segmentation.

        @param      img     initial image
        @return             new image
        """
        img = self._load_image(img)
        viz = fcn.utils.visualize_segmentation(
            lbl_pred=pred, img=img, n_class=self._n_class, label_names=self._class_name)
        return viz
