
.. index:: énoncé, vidéo, montage

.. _l-montage_video:

Petit trucage vidéo avec Python
===============================

A partir de 7 ans.

L'objectif de l'exercice est d'assembler des bouts de vidéos
existantes, qu'elles viennent de son téléphone ou de :epkg:`youtube`,
de changer la bande son, d'ajouter des inscrustations.
Si les exercices suivants peuvent être réalisés
avec :epkg:`moviepy`, des fonctions ont été implémentées
pour résoudre les exercices et sont décrites ici :
:ref:`l-api-video-audio`. Il ne s'agit pas d'écrire des programmes
compliqués mais plutôt de passer le plus de temps possible
sur la réalisation de petits films.

Mise en scène
-------------

On souhaite réaliser des trucages vidéos comme
celui de passer à travers un mur, de changer sa voix,
ou courir à toute allure. Ce jeu se joue à deux ou trois,
un metteur en scène, un ou deux acteurs.

.. video:: mur.mp4
    :width: 50%
    :height: 50%

Ce petit notebook pour vous aider tout au long
de l'atelier : :ref:`exemplevideodevoxx2018rst`.

Exercice 1 - passer à travers un mur
------------------------------------

#. Choisir un mur, supposer qu'on peut trafiquer un film,
   imaginer ce qu'il faudrait faire pour passer à travers
   un mur.
#. Filmer les séquences nécessaires.
#. Visionner les vidéos et noter à la seconde près les extraits
   des vidéos.
#. Extraire chaque bout avec la fonction
   :func:`video_extract_video <code_beatrix.faq.faq_video.video_extract_video>`.
#. Assembler chaque bout en une seule vidéo avec la fonction
   :func:`video_concatenate <code_beatrix.faq.faq_video.video_concatenate>`.
#. Enregister la vidéo avec la fonction
   :func:`video_save <code_beatrix.faq.faq_video.video_save>`.

Exercice 2 - ajouter du texte
-----------------------------

#. On reprend la vidéo précédente et on y incruste
   du texte et des images pour commenter ce que les personnages,
   pour s'en moquer ou font ou pour les doubler :
   :func:`video_text <code_beatrix.faq.faq_video.video_text>`.
#. Enregister la vidéo avec la fonction
   :func:`video_save <code_beatrix.faq.faq_video.video_save>`.

Exercice 3 - changer la musique
-------------------------------

#. Choisir une musique pour en faire une bande son,
   sur :epkg:`youtube` par exemple, avec le module :epkg:`pytube`
   ou la fonction :func:`download_youtube_video <code_beatrix.faq.faq_video.download_youtube_video>`.
#. Extraire la bande de la vidéo précédente avec la fonction
   :func:`video_extract_audio <code_beatrix.faq.faq_video.video_extract_audio>`.
#. S'il y a plusieurs sons, il faudra les concaténer la fonction
   :func:`audio_concatenate <code_beatrix.faq.faq_video.audio_concatenate>`.
#. Enregister la vidéo avec la fonction
   :func:`video_save <code_beatrix.faq.faq_video.video_save>`.

Exercice 4 - accélérer
----------------------

On reprend toutes les opérations pour un faire une seul programme
qu'on exécute pour vérifier qu'il donne bien la même chose qu'avant.
On accélère la vidéo obtenue avec la fonction
:func:`video_modification <code_beatrix.faq.faq_video.video_modification>`.

Solution
--------

Voir :ref:`l-montage_video_sol`.

A quoi ça sert ?
----------------

Démarrer sa propre chaîne :epkg:`youtube` et devenir
un célèbre *youtubeur* ou
`Vidéaste (web) <https://fr.wikipedia.org/wiki/Vid%C3%A9aste_(Web)>`_
et avoir sa propre chaîne comme
`Science Etonnante <https://www.youtube.com/channel/UCaNlbnghtwlsGF-KzAFThqA>`_.
