
.. index:: énoncé, vidéo, montage

.. _l-montage_video:

Petit montage vidéo avec Python
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

On souhaite réaliser un dialogue imaginaire à partir de
personnages qui appartiennent à des films ou à des vidéos
différentes.

Exercice 1
----------

#. Ecrire un petit scénario avec deux ou trois répliques
   qu'on pourra réaliser à partir de vidéos :epkg:`youtube`.
   On peut choisir des films, des chansons...
#. Télécharger les vidéos si besoin avec le module
   :epkg:`pytube` ou la fonction
   :func:`download_youtube_video <code_beatrix.faq.faq_video.download_youtube_video>`.
#. Visionner les vidéos et noter à la seconde près les extraits
   des vidéos.
#. Extraire chaque bout avec la fonction
   :func:`video_extract_video <code_beatrix.faq.faq_video.video_extract_video>`.
#. Assembler chaque bout en une seule vidéo avec la fonction
   :func:`video_concatenate <code_beatrix.faq.faq_video.video_concatenate>`.
#. Enregister la vidéo avec la fonction
   :func:`video_save <code_beatrix.faq.faq_video.video_save>`.

Exercice 2
----------

#. On reprend la vidéo précédente et on y inscrute
   du texte et des images pour commenter ce que les personnages,
   pour s'en moquer ou font ou pour les doubler.
   **fonction non implémentée**
#. Enregister la vidéo avec la fonction
   :func:`video_save <code_beatrix.faq.faq_video.video_save>`.

Exercice 3
----------

#. Extraire la bande de la vidéo précédente avec la fonction
   :func:`video_extract_audio <code_beatrix.faq.faq_video.video_extract_audio>`.
#. Choisir une musique pour en faire une bande son.
#. Superposer les deux sons avec la fonction
   :func:`audio_compose <code_beatrix.faq.faq_video.audio_compose>`.
#. Enregister la vidéo avec la fonction
   :func:`video_save <code_beatrix.faq.faq_video.video_save>`.

Exercice 4
----------

On reprend toutes les opérations pour un faire une seul programme
qu'on exécute pour vérifier qu'il donne bien la même chose qu'avant.
On choisit un des personnages et le faire parler deux plus vite
avec la fonction
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
