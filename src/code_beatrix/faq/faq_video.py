# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.
"""
from pytube import YouTube


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
