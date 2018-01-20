# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.
"""
import os
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.VideoClip import VideoClip
from moviepy.editor import VideoFileClip, AudioFileClip


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
        if isinstance(video_or_file, VideoContext):
            self.video_or_file = video_or_file.video
        else:
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
        elif isinstance(self.video_or_file, VideoContext):
            raise TypeError("Video cannot be a VideoContext")
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
                "Unable to find method '{0}' in {1}".format(fct, type(self.video)))
        return getattr(self.video, fct)


class AudioContext:
    """
    Creates a context for a :epkg:`AudioClip`.

    @return     :epkg:`AudioClip`
    """

    def __init__(self, audio_or_file):
        """
        @param      audio_or_file   string or :epkg:`AudioClip`
        """
        if isinstance(audio_or_file, AudioContext):
            self.audio_or_file = audio_or_file.audio
        else:
            self.audio_or_file = audio_or_file

    def __enter__(self):
        """
        Enters the context.
        """
        if isinstance(self.audio_or_file, str):
            if not os.path.exists(self.audio_or_file):
                raise FileNotFoundError(self.audio_or_file)
            audio = AudioFileClip(self.audio_or_file)
            self.close = True
        elif isinstance(self.audio_or_file, AudioClip):
            audio = self.audio_or_file
            self.close = False
        elif isinstance(self.audio_or_file, AudioContext):
            raise TypeError("Audio cannot be a VideoContext")
        else:
            raise TypeError(
                'Unable to use type {0}'.format(type(self.audio_or_file)))
        self.audio = audio
        return self

    def __exit__(self, *exc):
        """
        Leaves the context.
        """
        if exc and len(exc) == 3 and exc[1] is not None:
            raise exc[1]
        return False

    def __getattr__(self, fct):
        """
        Retrieves a method in :epkg:`AudioClip`.

        @param      fct     method name
        @return             method
        """
        if not hasattr(self.audio, fct):
            raise AttributeError(
                "Unable to find method '{0}' in {1}".format(fct, type(self.audio)))
        return getattr(self.audio, fct)


def get_wrapped(obj):
    """
    Retrives the video or the audio wrapped or not wrapped into obj.

    @param      obj     @see cl WrappedObject, @see cl AudioContext, @see cl VideoContext
    @return             wrapped object
    """
    if isinstance(obj, VideoContext):
        return obj.video
    elif isinstance(obj, AudioContext):
        return obj.audio
    else:
        return obj


def clean_video(video):
    """
    Cleans residual open streams.
    It is related to the following issues:

    * `The handle is invalid - Windows Only <https://github.com/Zulko/moviepy/issues/697>`_
    """
    if isinstance(video, str):
        raise TypeError("Unexpected type (string)")
    if hasattr(video, 'reader'):
        video.reader.close()
    if hasattr(video.audio, 'reader'):
        video.audio.reader.close_proc()
