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
import moviepy.audio.fx.all as afx
from moviepy.audio.AudioClip import AudioArrayClip, CompositeAudioClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from .moviepy_context import AudioContext, VideoContext

##########
# youtube
##########


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

########
# audio
########


def audio_extract_audio(audio_or_file, ta=0, tb=None):
    """
    Extracts a part of an audio.
    Extrait une partie du son.
    Uses `subclip <https://zulko.github.io/moviepy/ref/AudioClip.html?highlight=audioclip#moviepy.audio.AudioClip.AudioClip.subclip>`_.

    @param      audio_or_file   string or :epkg:`AudioClip`
    @param      ta              beginning
    @param      tb              end
    @return                     :epkg:`VideoClip`
    """
    with AudioContext(audio_or_file) as audio:
        return audio.subclip(ta, tb)


def audio_save(audio_or_file, filename, verbose=False, **kwargs):
    """
    Saves as a sound.
    Enregistre un son dans un fichier.
    Uses `write_audiofile <https://zulko.github.io/moviepy/ref/AudioClip.html?highlight=audioclip#moviepy.audio.AudioClip.AudioClip.write_audiofile>`_.

    @param      audio_or_file   string or :epkg:`AudioClip`
    @param      verbose         logging or not
    @param      kwargs          see `write_audiofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_
    """
    with AudioContext(audio_or_file) as audio:
        if verbose:
            audio.write_audiofile(filename, verbose=verbose, **kwargs)
        else:
            f = io.StringIO()
            with redirect_stdout(f):
                with redirect_stderr(f):
                    audio.write_audiofile(filename, verbose=verbose, **kwargs)


def audio_modification(new_sound, loop_duration=None, volumex=1.,
                       fadein=False, fadeout=False, t_start=0, t_end=None,
                       speed=1.):
    """
    Modifies a sound.
    Modifie un son.

    @param      loop_duration   loops sound
    @param      volumex         multiplies the sound
    @param      fadein          decreases the volume of the first seconds
    @param      fadeout         decreases the volume of the last seconds
    @param      t_start         shorten the audio
    @param      t_end           shorten the audio
    @param      speed           speed of the sound
    @return                     new sound
    """
    with AudioContext(new_sound) as audio:
        if speed:
            audio = audio.fl_time(lambda t: t * speed, keep_duration=True)
            wav = audio.to_soundarray(fps=audio.fps)
            audio = AudioArrayClip(wav, audio.fps)
        if volumex != 1.:
            audio = audio.fx(afx.volumex, volumex)
        if loop_duration:
            audio = afx.audio_loop(audio, duration=loop_duration)
        if fadein:
            audio = audio.fx(afx.audio_fadein, 1.0)
        if fadeout:
            audio = audio.fx(afx.audio_fadeout, 1.0)
        if t_start != 0 or t_end is not None:
            audio = audio.subclip(t_start=t_start, t_end=t_end)
        return audio


def audio_compose(audio_or_file1, audio_or_file2, t1=0, t2=None):
    """
    Concatenates or superposes two sounds.
    Ajoute ou superpose deux sons.

    @param      audio_or_file1      son 1
    @param      audio_or_file2      son 2
    @param      t1                  start of the first sound
    @param      t2                  start of the second sound (or None to add it ad
    @return                         new sound
    """
    with AudioContext(audio_or_file1) as audio1:
        with AudioContext(audio_or_file2) as audio2:
            add = []
            if t1 != 0:
                add.append(audio1.set_start(t1))
            else:
                add.append(audio1)
            if t2 is None:
                add.append(audio2.set_start(audio1.duration + t1))
            else:
                add.append(audio2.set_start(t2))
            return CompositeAudioClip(add)


########
# vidéo
########

def video_extract_video(video_or_file, ta=0, tb=None):
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


def video_save(video_or_file, filename, verbose=False, **kwargs):
    """
    Saves as a video or as a :epkg:`gif`.
    Enregistre une vidéo dans un fichier.
    Uses `write_videofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      verbose         logging or not
    @param      kwargs          see `write_videofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_
    """
    if isinstance(filename, str) and os.path.splitext(filename)[-1] == '.gif':
        with VideoContext(video_or_file) as video:
            if verbose:
                video.write_gif(filename, verbose=verbose, **kwargs)
            else:
                f = io.StringIO()
                with redirect_stdout(f):
                    with redirect_stderr(f):
                        video.write_gif(filename, verbose=verbose, **kwargs)
    else:
        with VideoContext(video_or_file) as video:
            if verbose:
                video.write_videofile(filename, verbose=verbose, **kwargs)
            else:
                f = io.StringIO()
                with redirect_stdout(f):
                    with redirect_stderr(f):
                        video.write_videofile(
                            filename, verbose=verbose, **kwargs)


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


def video_replace_sound(video_or_file, new_sound, **kwargs):
    """
    Replaces the sound of a video.
    Remplace la bande-son d'une vidéo.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      new_sound       sound
    @param      kwargs          see @see fn audio_modification
    @param      loop            if True, *loop_duration* becomes the duration of the video
    @return                     :epkg:`VideoClip`

    The list of available transformations is at:
    `vfx <https://zulko.github.io/moviepy/ref/videofx.html?highlight=vfx>`_.
    """
    with VideoContext(video_or_file) as video:
        if 'loop' in kwargs:
            kwargs['loop_duration'] = video.duration
            del kwargs['loop']
        audio = audio_modification(new_sound, **kwargs)
        new_clip = video.set_audio(audio)
        return new_clip


def video_extract_audio(video_or_file):
    """
    Returns the audio of a video.
    Retourne le son d'une vidéo.

    @param      video_or_file   string or :epkg:`VideoClip`
    @return                     :epkg:`AudioClip`
    """
    with VideoContext(video_or_file) as video:
        return video.audio


def video_compose(video_or_file1, video_or_file2, t1=0, t2=None, **kwargs):
    """
    Concatenates or superposes two videos.
    Ajoute ou superpose deux vidéos.

    @param      video_or_file1      vidéo 1
    @param      video_or_file2      vidéo 2
    @param      t1                  start of the first sound
    @param      t2                  start of the second sound (or None to add it ad
    @param      kwargs              additional parameters,
                                    sent to `CompositeVideoClip <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=compositevideoclip#compositevideoclip>`_
    @return                         new sound
    """
    with VideoContext(video_or_file1) as video1:
        with VideoContext(video_or_file2) as video2:
            add = []
            if t1 != 0:
                add.append(video1.set_start(t1))
            else:
                add.append(video1)
            if t2 is None:
                add.append(video2.set_start(video1.duration + t1))
            else:
                add.append(video2.set_start(t2))
            return CompositeVideoClip(add)
