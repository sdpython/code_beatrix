# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.
"""
from contextlib import redirect_stdout, redirect_stderr
import io
import os
from pytube import YouTube
from imageio import imsave
from moviepy.video.VideoClip import VideoClip
from moviepy.editor import VideoFileClip


def download_youtube_video(tag, output_path=None, res='720p', mime_type="video/mp4", **kwargs):
    """
    Downloads a video from :epkg:`youtube` with :epkg:`pytube`.
    Télécharge une vidéo depuis :epkg:`youtube` avec :epkg:`pytube`.

    @param      tag         tag of the :epkg:`youtube` video to download
    @param      output_path output path
    @param      mime_type   see :epkg:`youtube`
    @param      res         see :epkg:`youtube`
    @param      kwargs      see :epkg:`youtube`
    @return                 filename

    .. faqref::
        :title: Télécharger une vidéo sur YouTube

        Le module :epkg:`pytube` permet de télécharger une vidéo
        :epkg:`youtube`. Chaque vidéo est disponible selon plusieurs
        format dont on récupère la liste avant de choisir
        qui correspond à celui voulu.

        ::

            from pytube import YouTube
            yt = YouTube('https://www.youtube.com/watch?v=tRFHXMQP-QU')
            st = yt.streams
            fil = st.filter(mime_type="video/mp4", res="720p")
            fil.first().download()

    """
    yt = YouTube('https://www.youtube.com/watch?v={0}'.format(tag))
    st = yt.streams.filter(mime_type=mime_type, res=res, **kwargs)
    fi = st.first()
    fi.download(output_path=output_path)
    return fi.default_filename


class VideoContext:
    """
    Creates a context for a :epkg:`VideoClip`.
    It deals with opening, closing subprocesses.

    @return                     :epkg:`VideoClip`
    """

    def __init__(self, video_or_file):
        """
        @param      video_or_file   string or :epkg:`VideoClip`
        """
        self.video_or_file = video_or_file

    def __enter__(self):
        """
        Enters the context.
        """
        if isinstance(self.video_or_file, str):
            if not os.path.exists(self.video_or_file):
                raise FileNotFoundError(self.video_or_file)
            video = VideoFileClip(self.video_or_file)
            self.close = True
        elif isinstance(self.video_or_file, VideoClip):
            video = self.video_or_file
            self.close = False
        else:
            raise TypeError(
                'Unable to use type {0}'.format(type(self.video_or_file)))
        self.video = video
        return self

    def __exit__(self, *exc):
        """
        Leaves the context.
        """
        if exc and len(exc) == 3 and exc[1] is not None:
            raise exc[1]
        if self.close:
            del self.video
        return False

    def __getattr__(self, fct):
        """
        Retrieves a method in :epkg:`VideoClip`.

        @param      fct     method name
        @return             method
        """
        if not hasattr(self.video, fct):
            raise AttributeError(
                "Unable to find function '{0}' in {1}".format(fct, type(self.video)))
        return getattr(self.video, fct)


def extract_video(video_or_file, ta=0, tb=None):
    """
    Extracts a part of a video.
    Extrait une partie de la vidéo.
    Uses `subclip <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.VideoClip.VideoClip.subclip>`_.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      ta              beginning
    @param      tb              end
    @return                     :epkg:`VideoClip`
    """
    with VideoContext(video_or_file) as video:
        return video.subclip(ta, tb)


def save_video(video_or_file, filename, verbose=False, **kwargs):
    """
    Saves as a video.
    Enregistre une vidéo dans un fichier.
    Uses `write_videofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      verbose         logging or not
    @param      kwargs          see `write_videofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_
    """
    with VideoContext(video_or_file) as video:
        if verbose:
            video.write_videofile(filename, verbose=verbose, **kwargs)
        else:
            f = io.StringIO()
            with redirect_stdout(f):
                with redirect_stderr(f):
                    video.write_videofile(filename, verbose=verbose, **kwargs)


def video_enumerate_frames(video_or_file, folder=None, fps=10, pattern='images_%04d.jpg', **kwargs):
    """
    Enumerates frames from a video.
    Itère sur des images depuis une vidéo.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      folder          where to exports the images or returns arrays if None
    @param      pattern         image names
    @param      fps             frames per seconds
    @param      kwargs          arguments to `iter_frames <https://zulko.github.io/moviepy/ref/AudioClip.html?highlight=frames#moviepy.audio.AudioClip.AudioClip.iter_frames>`_
    @return                     iterator on arrays or files
    """
    with VideoContext(video_or_file) as video:
        if folder is None:
            for frame in video.iter_frames(fps=fps, **kwargs):
                yield frame
        else:
            if 'dtype' in kwargs:
                if kwargs['dtype'] != 'uint8':
                    raise ValueError("dtype must be uint8")
                else:
                    del kwargs['dtype']

            for i, frame in enumerate(video.iter_frames(fps=fps, dtype='uint8', **kwargs)):
                # saves as image
                name = os.path.join(folder, pattern % i)
                imsave(name, frame)
                yield name
