
.. blogpost::
    :title: Montage vidéo avec Python
    :keywords: montage, audio, sons, film, youtube
    :date: 2018-01-02
    :categories: video
    :lid: b-montage-video-2018

    Je me suis mis en tête d'initier des adolescents à la
    programmation en faisant du montage vidéo. Il est facile
    aujourd'hui de se filmer avec un téléphone portable ou une
    tablette mais il faut pouvoir retravailler les prises
    et les assembler si on souhaite réaliser un petit film.
    La programmation n'est sans doute le premier réflexe et je
    me doute que beaucoup iront chercher sur internet un logiciel
    permettant de faire cela. Cela veut dire aussi un certain
    coût d'apprentissage. Je n'ai pas essayé même si j'ai trouvé
    un logiciel tel que :epkg:`ShotCut`
    (voir `FramaLibre / montage <https://framalibre.org/recherche-par-crit-res?keys=montage>`_).
    Au lieu de ça, j'ai regardé s'il existait un module :epkg:`Python`
    qui me permettait de faire cela. J'ai trouvé
    :epkg:`moviepy` et surtout la
    `gallerie d'exemples <https://zulko.github.io/moviepy/examples/examples.html>`_
    qui donne une assez bonne idée de ce qu'on peut faire avec.

    Cette approche est plus coûteuse lorsqu'il s'agit de faire des opérations
    simples tels que mettre bout à bout ou extraire un extrait d'une vidéo
    puisque que l'outil qui permet de visualiser le résultat
    (comme :epkg:`VLC`) est différent de celui qu'on utilise pour
    construire ce qu'on peut (:epkg:`Python` dans mon cas).
    Néanmoins, cette approche est moins coûteuse lorsqu'il s'agit
    de faire un traitement complexe comme parcourir un film image
    par image, extraire les personnages et les insérer dans une autre
    vidéo. J'ai par exemple isolé
    :epkg:`Mary Poppins` du décor dans lequel elle danse.

    .. image:: image_mary_poppins_12_0.jpeg
        :width: 400

    Ce procédé s'appuie sur du :epkg:`deep learning` et je ne pense pas
    que cette fonctionnalité soit accessible depuis un logiciel de
    montage vidéo. Et si jamais ça l'était, cela serait sans doute via
    une interface utilisateur plutôt complexe. Et voici
    :epkg:`Mary Poppins` sur une plage.

    .. image:: image_mary_poppins_29_1.png

    Ce qu'on souhaite faire est souvent un assemblage plus ou moins
    long de tâche simple et c'est assez facile à écrire qu'on on dispose
    d'un moyen d'enchaîner ces tâches simples. Le résultat est
    parfois complexe et si l'interface utilisateur existait, elle ferait
    apparaître de nombreuses options qui feraient probablement un peu
    peur au premier regard. C'est mon expérience, je ne dis pas que ce
    soit la seule, mais je pense qu'on passe moins de temps à explorer
    toutes les options ou contourner les limites de l'outil
    qu'on utilise en passant directement par
    la programmation plutôt que par un logiciel tout fait.
    Cela se traduit néanmoins par une approche un peu plus abstraite.
    A l'usage, on se sert des deux outils.

    Pour préparer ce travail, j'ai cherché à écrire un peu de lignes
    une façon de récupérer une vidéo, d'en extrait un bout,
    d'y ajouter une bande son, quelques incrustations textuelles.
    Cela m'a permis de constituer une petite liste de fonctions
    dont on peut s'inspirer : :ref:`l-api-video-audio` et quelques jeux
    :ref:`l-medias`. Quelques notebooks qui pourraient vous intéresser :
    :ref:`imagemarypoppinsrst`, :ref:`imagesegmentationrst`.
