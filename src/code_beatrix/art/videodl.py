# -*- coding: utf-8 -*-
"""
@file
@brief Fonctions proposant de traiter des vidéos
avec des traitements compliqués type
:epkg:`deep learning`.
"""
import os
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from ..ai import DLImageSegmentation
from .video import video_enumerate_frames
from .moviepy_context import VideoContext


def video_map_images(video_or_file, name, fLOG=None, **kwargs):
    """
    Applies one complex process to a video such as
    extracting characters from videos and
    removing the backaground. It is done image by image.
    Applique un traitement compliqué sur une séquence
    d'images telle que la séparation des personnages et du fond.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      name            name of the processing to do,
                                see the list below
    @param      fLOG            logging function
    @param      kwargs          additional parameters
    @return                     :epkg:`VideoClip`

    List of available treatments:

    * ``'people'``: extracts characters from a movie.
      The movie is composed with an image and a
      `mask <https://zulko.github.io/moviepy/ref/AudioClip.html?highlight=mask#moviepy.audio.AudioClip.AudioClip.set_ismask>`_.
      Parameters: see @fn video_map_images_people.
    * ``'detect'`` : blurs or put a rectangle around faces, uses :epkg:`opencv`

    .. warning:: A couple of errors timeout, out of memory...
        The following processes might be quite time consuming
        or memory consuming. If it is the case, you should think
        of reducing the resolution, the number of frames per seconds
        (*fps*). You can also split the video and process each piece
        independently and finally concatenate them.
    """
    allowed = {'people'}
    if name == 'people':
        return video_map_images_people(video_or_file, fLOG=fLOG, **kwargs)
    elif name == "detect":
        return video_map_images_detect(video_or_file, fLOG=fLOG, **kwargs)
    else:
        raise ValueError("Unknown process '{}', should be among: {}".format(
            name, ','.join(allowed)))


def video_map_images_people(video_or_file, resize=('max2', 400), fps=None,
                            with_times=False, progress_bar=False, dtype=None,
                            class_to_keep=15, fLOG=None, **kwargs):
    """
    Extracts characters from a movie.
    The movie is composed with an image and a
    `mask <https://zulko.github.io/moviepy/ref/AudioClip.html?highlight=mask#moviepy.audio.AudioClip.AudioClip.set_ismask>`_.
    Extrait les personnages d'un film, le résultat est
    composé d'une image et d'un masque transparent
    qui laissera apparaître l'image d'en dessous si cette
    vidéo est aposée sur une autre.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      resize          see :meth:`predict <code_beatrix.ai.image_segmentation.DLImageSegmentation.predict>`
    @param      fps             see @see fn video_enumerate_frames
    @param      with_times      see @see fn video_enumerate_frames
    @param      progress_bar    see @see fn video_enumerate_frames
    @param      dtype           see @see fn video_enumerate_frames
    @param      class_to_keep   class to keep from the image, it can
                                a number (15 for the background, a list of classes,
                                a function which takes an image and the prediction
                                and returns an image)
    @param      fLOG            logging function
    @param      kwargs          see @see cl DLImageSegmentation
    @return                     :epkg:`VideoClip`

    .. warning:: A couple of errors timeout, out of memory...
        The following processes might be quite time consuming
        or memory consuming. If it is the case, you should think
        of reducing the resolution, the number of frames per seconds
        (*fps*). You can also split the video and process each piece
        independently and finally concatenate them.

    .. exref::
        :title: Extract characters from a video.

        The following example shows how to extract a movie with
        people and without the background. It works better
        if the contrast between the characters and the background is
        high.

        ::

            from code_beatrix.art.video import video_extract_video, video_save
            from code_beatrix.art.videodl import video_map_images

            vide = video_extract_video("something.mp4", 0, 5)
            vid2 = video_map_images(vide, fps=10, name="people", progress_bar=True)
            video_save(vid2, "people.mp4")

        The function returns something like the the following.
        The character is wearing black and the background is quite
        dark too. That explains that the kind of large halo
        around the character.

        .. video:: videodl.mp4
    """
    if isinstance(class_to_keep, int):
        def local_mask(img, pred):
            img[pred != class_to_keep] = 0
            return img
    elif isinstance(class_to_keep, (set, tuple, list)):
        def local_mask(img, pred):
            dist = set(pred.ravel())
            rem = set(class_to_keep)
            for cl in dist:
                if cl not in rem:
                    img[pred == cl] = 0
            return img
    elif callable(class_to_keep):
        local_mask = class_to_keep
    else:
        raise TypeError("class_to_keep should be an int, a list or a function not {0}".format(
            type(class_to_keep)))

    if fLOG:
        fLOG('[video_map_images_people] loads deep learning model')
    model = DLImageSegmentation(fLOG=fLOG, **kwargs)
    iter = video_enumerate_frames(video_or_file, fps=fps, with_times=with_times,
                                  progress_bar=progress_bar, dtype=dtype, clean=False)
    if fLOG is not None:
        if fps is not None:
            every = max(fps, 1)
            unit = 's'
        else:
            every = 20
            unit = 'i'

    if fLOG:
        fLOG('[video_map_images_people] starts extracting characters')
    seq = []
    for i, img in enumerate(iter):
        if not progress_bar and fLOG is not None and i % every == 0:
            fLOG('[video_map_images_people] process %d%s images' % (i, unit))
        if resize is not None and isinstance(resize[0], str):
            if len(img.shape) == 2:
                resize = DLImageSegmentation._new_size(img.shape, resize)
            else:
                resize = DLImageSegmentation._new_size(img.shape[:2], resize)
        img, pred = model.predict(img, resize=resize)
        img2 = local_mask(img, pred)
        seq.append(img2)
    if fLOG:
        fLOG('[video_map_images_people] done.')

    return ImageSequenceClip(seq, fps=fps)


def video_map_images_detect(video_or_file, fps=None, with_times=False, progress_bar=False, dtype=None,
                            scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                            action='blur', color=(255, 255, 0), haar=None, fLOG=None):
    """
    Blurs people faces.
    Uses function `detectmultiscale <https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale>`_.
    Relies on :epkg:`opencv`.
    Floute les visages.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      fps             see @see fn video_enumerate_frames,
                                faces are detected in each frame returned by
                                @see fn video_enumerate_frames
    @param      with_times      see @see fn video_enumerate_frames
    @param      progress_bar    see @see fn video_enumerate_frames
    @param      dtype           see @see fn video_enumerate_frames
    @param      fLOG            logging function
    @param      scaleFactor     see `detectmultiscale <https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale>`_
    @param      minNeighbors    see `detectmultiscale <https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale>`_
    @param      minSize         see `detectmultiscale <https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale>`_
    @param      haar            shape classifier to load, face by default, see below
    @param      action          to blur, to put a rectangle around the detected zone... see below
    @param      color           rectangle color if *action* is ``'rect'``
    @return                     :epkg:`VideoClip`

    Only ``haarcascade_frontalface_alt.xml`` is provided but you can
    get more at `haarcascades <https://github.com/opencv/opencv/blob/master/data/haarcascades/>`_.

    Parameter *action* can be:

    * ``'blur'``: to blur faces (or detector zones)
    * ``'rect'``: to draw a rectangle around faces (or detector zones)

    .. exref::
        :title: Faces in a yellow box in a video

        The following example uses :epkg:`opencv` to detect faces
        on each image of a video and put a yellow box around each of them.

        ::

            from code_beatrix.art.videodl import video_map_images
            from code_beatrix.art.video import video_save, video_extract_video

            vide = video_extract_video(vid, 0, 5 if __name__ == "__main__" else 1)
            vid2 = video_map_images(
                vide, fps=10, name='detect', action='rect',
                progress_bar=True, fLOG=fLOG)
            exp = os.path.join(temp, "people.mp4")
            video_save(vid2, exp, fps=10)

        The following video is taken from
        `Charlie Chaplin's movies <source: https://www.youtube.com/watch?v=n_1apYo6-Ow>`_.

        .. video:: face.mp4
    """
    from cv2 import CascadeClassifier, CASCADE_SCALE_IMAGE
    from .video_drawing import blur, rectangle

    def fl_blur(gf, t, rects):
        im = gf(t)
        ti = min(int(t * fps), len(rects) - 1)
        rects = all_rects[ti]
        for rect in rects:
            x1, y1, dx, dy = rect
            blur(im, (x1, y1), (x1 + dx, y1 + dy))
        return im

    def fl_rect(gf, t, rects):
        im = gf(t)
        ti = min(int(t * fps), len(rects) - 1)
        rects = all_rects[ti]
        for rect in rects:
            x1, y1, dx, dy = rect
            rectangle(im, (x1, y1), (x1 + dx, y1 + dy), color)
        return im

    fcts = dict(blur=fl_blur, rect=fl_rect)

    if action not in fcts:
        raise ValueError("action='{0}' should be in {1}".format(
            action, list(sorted(fcts.keys()))))

    if fLOG:
        fLOG('[video_map_images_blur] detect faces')

    if haar is None:
        this = os.path.abspath(os.path.dirname(__file__))
        cascade_fn = os.path.join(
            this, 'data', 'haarcascade_frontalface_alt.xml')
    elif not os.path.exists(haar):
        raise FileNotFoundError(haar)
    else:
        cascade_fn = haar

    cascade = CascadeClassifier(cascade_fn)

    iter = video_enumerate_frames(video_or_file, fps=fps, with_times=with_times,
                                  progress_bar=progress_bar, dtype=dtype, clean=False)

    if fLOG:
        fLOG("[video_map_images_people] starts detecting and burring faces with: {0}".format(
            cascade_fn))
        if fps is not None:
            every = max(fps, 1)
            unit = 's'
        else:
            every = 20
            unit = 'i'

    all_rects = []
    for i, img in enumerate(iter):
        if not progress_bar and fLOG is not None and i % every == 0:
            fLOG('[video_map_images_face] process %d%s images' % (i, unit))

        try:
            rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                             minNeighbors=minNeighbors, minSize=minSize,
                                             flags=CASCADE_SCALE_IMAGE)
        except Exception as e:
            if fLOG:
                fLOG('Unable to retrieve any shape due to ', e)
            rects = []
        all_rects.append(rects)

    if fLOG:
        non = sum(map(len, (filter(lambda x: len(x) > 0, all_rects))))
        fLOG('[video_map_images_blur] creates video nb image: {1}, nb faces: {0}'.format(
            non, len(all_rects)))

    with VideoContext(video_or_file) as video:
        return video.video.fl(lambda im, t: fcts[action](im, t, all_rects), keep_duration=True)
