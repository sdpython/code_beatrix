
.. index:: énoncé, algorithme, orange, tri

.. _l-algo_orange:

Le jeu des oranges
==================

A partir de 7-8 ans (mais ce n'est qu'une indication).

C'est un petit jeu où il faut être inventif
pour construire la méthode qui aboutit à la solution.
Il est préférable d'avoir compris ce qu'est un :ref:`tri <l-algo_tri>` au préalable.

Mise en scène
-------------

Cinq enfants sont placés autour d'un cercle.
Chacun a un numéro.
Il y a neuf orange numérotées, deux numéros 1, deux 2, deux 3, deux 4, un numéro 5
(ça marche aussi avec des couleurs).
Au début chaque enfant prend deux oranges au hasard dans chaque main sauf le dernier.

Règle :

    A chaque tour, seul l'enfant qui a une main vide peut recevoir une orange
    d'un de ses deux voisins.

    Seul l'enfant qui a une main vide peut changer son orange de main.

Objectif :

    A la fin du jeu, chaque enfant doit avoir dans ses mains
    les oranges portant son numéro.

Une petite histoire
-------------------

Arriver à la solution sans tricher peut s'avérer compliqué. De plus,
comment décrire un algorithme lorsque le vocabulaire de ce petit jeu
consiste à dire quel voisin doit passer une orange à celui qui n'en a pas.

La première chose à faire est d'y mettre un peu d'ordre et d'inventer
un langage un peu plus évolué. Pour raconter l'histoire,
il faut que chaque enfant se tienne de profil et représenter le problème
comme deux cercles d'oranges dont l'un est incomplet puisqu'il manque une orange.

.. image:: orange1.png

**Q1 :** Comment faire tourner un cercle ?

**Q2 :** Comment faire tourner l'autre cercle ?

A partir de maintenant, on ne dira plus qu'il faut passer telle orange
à la main vide mais on dira une de ces phrases :

* Le cercle intérieur tourne de 1,2,3,... pas dans le sens inverse ou pas des aiguilles d'une montre.
* Le cercle extérieur tourne de 1,2,3,... dans le sens inverse ou pas des aiguilles d'une montre.
* Celui qui a une main vide change l'orange qu'il détient dans l'autre main.

On a maintenant tous les pièces de l'engrenage. Il ne manque plus qu'une astuce pour résoudre
l'énigme. Un dernier indice :

**Q3 :** en supposant qu'un a réussi à résoudre l'énigme et que les oranges sont revenues
à la bonne place, peut-on avoir deux fois le même numéro sur le même cercle ?

Solution
--------

Voir :ref:`l-algo_orange_sol`.

A quoi ça sert ?
----------------

Connaissez-vous le `Rubik's cube <http://fr.wikipedia.org/wiki/Rubik%27s_Cube>`_ ?
Si les deux jeux ne sont pas vraiment reliés, cela permet de comprendre
que pour réussir, il faut parfois en apparence défaire ce qui a été fait.
