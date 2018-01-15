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


class AudioContext:
    """
    Creates a context for a :epkg:`AudioClip`.

    @return     :epkg:`AudioClip`
    """

    def __init__(self, audio_or_file):
        """
        @param      audio_or_file   string or :epkg:`AudioClip`
        """
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
                "Unable to find function '{0}' in {1}".format(fct, type(self.audio)))
        return getattr(self.audio, fct)
