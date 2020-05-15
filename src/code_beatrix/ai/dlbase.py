"""
@file
@brief Base class for deep learning models.
"""
import os


class DeepLearningBase:
    """
    Implements a common interface to manipulate pre-trained
    deep learning models.
    """

    def __init__(self, model, gpu, fLOG=None):
        """
        @param      model       model (url, filename, ...)
        @param      gpu         use gpu
        @param      fLOG        logging function
        """
        self._gpu = gpu
        if model is None:
            raise ValueError("model must be specified")
        if isinstance(model, str):
            if not os.path.exists(model):
                raise FileNotFoundError("Unable to find '{0}'".format(model))
            raise NotImplementedError(
                "Unable to load model '{0}'".format(model))
        self._model = model
        self._fLOG = fLOG

    def log(self, *args, **kwargs):
        """
        Log something.
        """
        if self._fLOG:
            self._fLOG(*args, **kwargs)

    def predict(self, X):
        """
        Applies the model on features *X*.

        @param      X       features
        @return             prediction
        """
        raise NotImplementedError("Method predict is not implemented.")


class DeepLearningImage(DeepLearningBase):
    """
    Implements a common interface to manipulate pre-trained
    deep learning models processing images.
    """

    def __init__(self, model, gpu=False, fLOG=None):
        """
        @param      model       model name
        @param      gpu         use gpu
        @param      fLOG        logging function
        """
        DeepLearningBase.__init__(self, model, gpu=gpu, fLOG=fLOG)
