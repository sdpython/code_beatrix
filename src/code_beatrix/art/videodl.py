# -*- coding: utf-8 -*-
"""
@file
@brief Fonctions proposant de traiter des vidéos
avec des traitements compliqués type
:epkg:`deep learning`.
"""
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from ..ai import DLImageSegmentation
from .video import video_enumerate_frames


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
                                  progress_bar=progress_bar, dtype=dtype)
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
