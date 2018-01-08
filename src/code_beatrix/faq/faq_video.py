# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.
"""
from contextlib import redirect_stdout, redirect_stderr
import io
import os
import sys
import numpy
from pytube import YouTube
from imageio import imsave
import moviepy.audio.fx.all as afx
import moviepy.video.fx.all as vfx
from moviepy.video.VideoClip import ImageClip, VideoClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.audio.AudioClip import AudioArrayClip, CompositeAudioClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.audio.AudioClip import concatenate_audioclips
from .moviepy_context import AudioContext, VideoContext
from PIL import Image, ImageFont, ImageDraw
from skimage.io._plugins.pil_plugin import pil_to_ndarray
from skimage.transform import rescale


class FontError(Exception):
    """
    Raised when a font cannot be found.
    """
    pass


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

    Example:

    ::

        from code_beatrix.faq.faq_video import audio_extract_audio
        son = audio_extract_audio('son.mp3', '00:00:01', '00:00:02')
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


def audio_modification(audio, loop_duration=None, volumex=1.,
                       fadein=False, fadeout=False, t_start=0, t_end=None,
                       speed=1.):
    """
    Modifies a sound.
    Modifie un son.

    @param      audio           sound
    @param      loop_duration   loops sound
    @param      volumex         multiplies the sound
    @param      fadein          decreases the volume of the first seconds
    @param      fadeout         decreases the volume of the last seconds
    @param      t_start         shorten the audio
    @param      t_end           shorten the audio
    @param      speed           speed of the sound
    @return                     new sound
    """
    with AudioContext(audio) as audio:
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

    Example:

    ::

        from code_beatrix.faq.faq_video import audio_compose
        son = audio_compose('son1.mp3', 'son2.mp3', 0, 10)
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


def audio_concatenate(audio_or_files, **kwargs):
    """
    Concatenates sounds.
    Met bout à bout des sons.

    @param      audio_or_files  list of sounds or filenames
    @param      kwargs          additional parameters for
                                `concatenate_audioclips <https://github.com/Zulko/moviepy/blob/master/moviepy/audio/AudioClip.py#L308>`_
    @return                     :epkg:`VideoClip`

    Example:

    ::

        from code_beatrix.faq.faq_video import audio_concatenate
        son = audio_concatenate('son1.mp3', 'son2.mp3')
    """
    ctx = [AudioContext(_).__enter__() for _ in audio_or_files]
    res = concatenate_audioclips([_.audio for _ in ctx], **kwargs)
    for _ in ctx:
        _.__exit__()
    return res

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

    Example:

    ::

        from code_beatrix.faq_faq_video import video_extract_video
        vid = video_extract_video('exemple.mp4', '00:00:01', '00:00:04')
    """
    with VideoContext(video_or_file) as video:
        return video.subclip(ta, tb)


def video_save(video_or_file, filename, verbose=False, duration=None, **kwargs):
    """
    Saves as a video or as a :epkg:`gif`.
    Enregistre une vidéo dans un fichier.
    Uses `write_videofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      duration        overwrite duration,
                                see method `set_duration <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videoclip#moviepy.video.VideoClip.VideoClip.set_duration>`_
    @param      verbose         logging or not
    @param      kwargs          see `write_videofile <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=videofileclip#moviepy.video.io.VideoFileClip.VideoFileClip.write_videofile>`_

    Example:

    ::

        from code_beatrix.faq_faq_video import video_extract_video, video_save
        vid = video_extract_video('exemple.mp4', '00:00:01', '00:00:04')
        video_save(vid, 'new_video.mp4')
    """
    if isinstance(filename, str) and os.path.splitext(filename)[-1] == '.gif':
        with VideoContext(video_or_file) as video:
            if duration is not None:
                video = video.set_duration(duration)
            if verbose:
                video.write_gif(filename, verbose=verbose, **kwargs)
            else:
                f = io.StringIO()
                with redirect_stdout(f):
                    with redirect_stderr(f):
                        video.write_gif(filename, verbose=verbose, **kwargs)
    else:
        with VideoContext(video_or_file) as video:
            if duration is not None:
                video = video.set_duration(duration)
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
    @return                     iterator on arrays or files (see parameter *folder*)

    Example:

    ::

        form code_beatrix.faq.faq_video import video_enumerate_frames
        vid = 'example.mp4')
        for frame in video_enumerate_frames(vid, folder=temp):
            # ...

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


def video_replace_audio(video_or_file, new_sound, **kwargs):
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

    Example:

    ::

        from code_beatrix.faq.faq_video import video_replace_sound
        vid = video_replace_sound('video.mp4', 'son.mp3', loop=True, volumex=5.5, t_end='00:00:05')
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


def video_remove_audio(video_or_file):
    """
    Returns the same video without audio.
    Retourne la même vidéo sans le son.

    @param      video_or_file   string or :epkg:`VideoClip`
    @return                     :epkg:`AudioClip`
    """
    with VideoContext(video_or_file) as video:
        return video.without_audio()


def video_compose(video_or_file1, video_or_file2=None, t1=0, t2=0, **kwargs):
    """
    Concatenates or superposes two videos.
    Ajoute ou superpose deux vidéos.

    @param      video_or_file1      vidéo 1 or list of video
    @param      video_or_file2      vidéo 2
    @param      t1                  start of the first sound
    @param      t2                  start of the second sound (or None to add it ad
    @param      kwargs              additional parameters,
                                    sent to `CompositeVideoClip <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=compositevideoclip#compositevideoclip>`_
    @return                         :epkg:`VideoClip`

    Example:

    ::

        from code_beatrix.faq.faq_video import video_compose
        vid = video_compose('video1.mp4', 'video2.mp4', '00:00:01', '00:00:04')

    The first video defines the size of the final video.
    """
    if isinstance(video_or_file1, list):
        if video_or_file2 is not None:
            raise ValueError(
                'video_or_file1 is a list, video_or_file2 should be None')
        vids = [VideoContext(i).__enter__() for i in video_or_file1]
        comp = []
        for i, v in enumerate(vids):
            v = v.video
            if isinstance(t1, list) and i < len(t1):
                v.set_start(t1[i])
            comp.append(v)
        res = CompositeVideoClip(comp, **kwargs)
        for v in vids:
            v.__exit__()
        return res
    else:
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
                return CompositeVideoClip(add, **kwargs)


def video_concatenate(video_or_files, **kwargs):
    """
    Concatenates videos.
    Met bout à bout des vidéos.

    @param      video_or_files  list of videos or filenames
    @param      kwargs          additional parameters for
                                `concatenate_videoclips <https://github.com/Zulko/moviepy/blob/master/moviepy/video/compositing/concatenate.py#L15>`_
    @return                     :epkg:`VideoClip`
    """
    ctx = [VideoContext(_).__enter__() for _ in video_or_files]
    res = concatenate_videoclips([_.video for _ in ctx], **kwargs)
    for _ in ctx:
        _.__exit__()
    return res


def video_modification(video_or_file, volumex=1., resize=1., speed=1.,
                       mirrorx=False, mirrory=False, method=None):
    """
    Modifies a video.
    Modifie une vidéo.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      volumex         multiplies the sound
    @param      speed           speed of the sound
    @param      resize          resize
    @param      mirrorx         mirror x
    @param      mirrory         mirror y
    @param      method          method used to resize
    @return                     new video

    Example:

    ::

        from code_beatrix.faq.faq_video import video_modification
        vid = video_modification('video.mp4', speed=2., mirrory=True, mirrorx=True)
    """
    def check_duration(video):
        if video.duration is None:
            raise ValueError('video duration should not be None')

    with VideoContext(video_or_file) as video:
        if speed:
            check_duration(video)
            dur = video.duration
            video = video.fl_time(lambda t: t * speed)
            video = video.set_duration(dur / speed)
        if volumex != 1.:
            video = video.fx(vfx.volumex, volumex)
        if resize != 1.:
            if method is not None:
                video = video.fx(vfx.resize, resize)
            else:
                video = video.fx(vfx.resize, resize, method=method)
        if mirrorx:
            video = video.fx(vfx.mirror_x)
        if mirrory:
            video = video.fx(vfx.mirror_y)
        return video


def video_image(image_or_file, duration=None, zoom=None, opacity=None, **kwargs):
    """
    Creates a :epkg:`ImageClip`.
    Créé une vidéo à partir d'une image.

    @param      image_or_file   image or file
    @param      duration        duration or None if not known
    @param      zoom            applies a zoom on the image
    @param      opacity         opacity of the image (0 for transparent, 255 for opaque)
    @param      kwargs          additional parameters for :epkg:`ImageClip`
    @return                     :epkg:`ImageClip`

    If *duration* is None, it will be fixed when the image is
    composed with another one. The image remains wherever it is placed.
    """
    if isinstance(image_or_file, str):
        img = Image.open(image_or_file)
        return video_image(img, duration=duration, zoom=zoom, opacity=opacity, **kwargs)
    elif isinstance(image_or_file, numpy.ndarray):
        if zoom is not None:
            img = rescale(image_or_file, zoom)
            return video_image(img, duration=duration, opacity=opacity, **kwargs)
        else:
            img = image_or_file
            if len(img.shape) != 3:
                raise ValueError(
                    "Image is not RGB or RGBA shape={0}".format(img.shape))
            if img.shape[2] == 3:
                pilimg = Image.fromarray(img).convert('RGBA')
                img = pil_to_ndarray(pilimg)
                if opacity is None:
                    opacity = 255
            if isinstance(opacity, int):
                img[:, :, 3] = opacity
            elif isinstance(opacity, float):
                img[:, :, 3] = int(opacity * 255)
            elif opacity is not None:
                raise TypeError("opacity should be int or float or None")
            return ImageClip(img, duration=duration, transparent=True, **kwargs)
    elif isinstance(image_or_file, Image.Image):
        if image_or_file.mode != 'RGBA':
            image_or_file = image_or_file.convert('RGBA')
        if zoom is not None:
            image_or_file = image_or_file.resize(zoom)
        img = pil_to_ndarray(image_or_file)
        return video_image(img, duration=duration, opacity=opacity, **kwargs)
    else:
        raise TypeError(
            "Unable to create a video from type {0}".format(type(image_or_file)))


def video_position(video_or_file, pos, relative=False):
    """
    Modifies the position of a position.
    Modifie la position d'une video.
    Relies on function
    `set_position <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=imageclip#moviepy.video.VideoClip.VideoClip.set_position>`_.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      pos             see `set_position <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=imageclip#moviepy.video.VideoClip.VideoClip.set_position>`_
    @param      relative        see `set_position <https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=imageclip#moviepy.video.VideoClip.VideoClip.set_position>`_
    @return                     :epkg:`VideoClip`

    This function moves the video inside another one.
    Therefore, it has no effect if the result of this video
    is composed. See function @see fn video_compose.
    Example:

    ::

        from code_beatrix.faq.faq_video import video_image, video_position, video_compose, video_text

        img = 'GastonLagaffe_1121.jpg'
        vidimg = video_image(img, duration=5, opacity=200)
        vidimg = video_position(vidimg, lambda t: (0, 0), relative=True)

        text = video_text('boule', size=2., color=(255, 0, 0, 128), background=(0, 255, 0, 100))
        text = video_position(text, lambda t: (t * 0.1, t * 0.2), relative=True)

        comb = video_compose([vidimg, text], t1=[0, 1])

    You can see an example of the video it produces in notebook
    :ref:`video_notebook`.
    """
    with VideoContext(video_or_file) as video:
        video = video.set_position(pos=pos, relative=relative)
        return video


def video_resize(video_or_file, newsize):
    """
    Resizes a video.
    Modifie la taille d'une video.
    Relies on function
    `resize <https://zulko.github.io/moviepy/ref/videofx/moviepy.video.fx.all.resize.html#moviepy.video.fx.all.resize>`_.

    @param      video_or_file   string or :epkg:`VideoClip`
    @param      newsize         `resize <https://zulko.github.io/moviepy/ref/videofx/moviepy.video.fx.all.resize.html#moviepy.video.fx.all.resize>`_
    @return                     :epkg:`VideoClip`
    """
    with VideoContext(video_or_file) as video:
        video = video.resize(newsize)
        return CompositeVideoClip([video])


def video_text(text, font=None, fontsize=32, size=None,
               color=None, background=None, opacity=None,
               **kwargs):
    """
    Creates an image with text (:epkg:`ImageClip`).
    Créé une image à partir de texte.

    @param      text            text
    @param      color           color
    @param      font            police name
    @param      fontsize        font size
    @param      size            image size, None to get the smallest one which
                                contains the text, a float to get *size* times
                                this smallest size
    @param      backgorund      background of the image
    @param      opacity         to overwrite the opacity,
                                *color* and *background* should be 4-uple colors,
                                the last number in ``(0, 0, 0, 255)`` represents the
                                opacity
    @param      kwargs          additional parameters sent to @see fn video_image
    @return                     :epkg:`ImageClip`

    If *duration* is None, it will be fixed when the image is
    composed with another one. The image remains wherever it is placed.
    The *opacity* is a number between 0 (transparent) and 255 (opaque).
    0 means the image cannot be seen. The number can be set up for each
    pixel. By default, the image background is transparent (0). You can find
    many font at `google/fonts <https://github.com/google/fonts/tree/master/ofl>`_
    or `msfonts <https://github.com/caarlos0-graveyard/msfonts/tree/master/fonts>`_.
    """
    if background is None:
        background = (255, 255, 255, 0)
    if color is None:
        color = (0, 0, 0, 255)
    if isinstance(font, str):
        if not font.endswith('.ttf'):
            font += '.ttf'
    elif font is None:
        if sys.platform.startswith('win'):
            font = "arial.ttf"
        else:
            exp = os.path.expanduser('~')
            d = os.path.join(exp, '.local', 'share', 'fonts')
            if not os.path.exists(d):
                raise FileNotFoundError("Unable to find '{0}'".format(d))
            font = os.path.join(d, "Ubuntu-Regular.ttf")
            if not os.path.exists(font):
                raise FileNotFoundError("Unable to find font '{0}'. Available:\n{1}".format(
                    font, "\n".join(os.listdir(d))))
    try:
        obj = ImageFont.truetype(font=font, size=fontsize)
    except OSError as e:
        raise FontError("Unable to find font '{0}'".format(font)) from e
    if size is None:
        size = obj.getsize(text)
    elif isinstance(size, (float, int)):
        fs = obj.getsize(text)
        size = (int(fs[0] * size), int(fs[1] * size))
    elif not isinstance(size, tuple):
        raise TypeError("size should be a tuple or a float")
    if opacity is not None:
        if len(color) == 3:
            color = color + (opacity,)
        elif len(color) == 4:
            color = color[:3] + (opacity,)
        else:
            raise ValueError("color should a 3 or 4 tuple")
    img = Image.new('RGBA', size, background)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=obj, fill=color)
    return video_image(img, **kwargs)


def video_frame(fct_frame, **kwargs):
    """
    Creates a video from drawing or images.
    *fct_frame* can either be a function which draws a picture at time *t*
    or a list of picture names or a folder.
    Créé une vidéo à partir de dessins ou d'images.
    *fct_frame* est soit une fonction qui dessine chaque image à chaque instant *t*,
    une liste de noms d'images ou un répertoire.

    @param      fct_frame       function like ``def make_frame(t: float) -> numpy.ndarray``,
                                or list of images or folder name
    @param      kwargs          additional arguments for function
                                `make_frame <https://zulko.github.io/moviepy/getting_started/videoclips.html#videoclip>`_
    @return                     :epkg:`VideoClip`
    """
    if isinstance(fct_frame, str):
        if not os.path.exists(fct_frame):
            raise FileNotFoundError(
                "Unable to find folder '{0}'".format(fct_frame))
        imgs = os.listdir(fct_frame)
        exts = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
        imgs = [os.path.join(fct_frame, _)
                for _ in imgs if os.path.splitext(_)[-1].lower() in exts]
        return video_frame(imgs, **kwargs)
    elif isinstance(fct_frame, list):
        for img in fct_frame:
            if not os.path.exists(img):
                raise FileNotFoundError(
                    "Unable to find image '{0}'".format(img))
        return ImageSequenceClip(fct_frame, **kwargs)
    else:
        return VideoClip(fct_frame, **kwargs)
