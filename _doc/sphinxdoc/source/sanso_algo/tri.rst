
.. index:: énoncé, algorithme, tri, Dunkerque 2015-03-25

.. _l-algo_tri:

Tri
===

A partir de 7-8 ans (mais ce n'est qu'une indication).

Trier, ordonner, ranger, autant de mots pour désigner le fait de s'arranger
pour retrouver facilement les choses qu'on a trié. Comment retrouver un livre s'ils
ne sont pas triés, comment retrouver ses clés si la maison est sens dessus dessous ?

Mise en scène
-------------

**retrouver des cartes**

On mélange un jeu de cartes puis on enlève trois cartes sans les montrer.
On tend le jeu de cartes à 4 personnes qui doivent déterminer les cartes qui manquent.
Les cartes sont parfois trompeuses, elles peuvent ressembler à ça :

.. image:: cartes1.jpg
    :width: 500 px

ou ça :

.. image:: cartes2.jpg
    :width: 500 px

**trier**

Même exercice mais on trie d'abord le jeu de cartes. On enlève ensuite trois cartes.
Il faut de nouveau deviner les cartes qui manquent. S'il y a deux groupes d'enfants,
l'un peut recevoir un jeu trié, l'autre non.

**Comment trier ?**

Dans un premier temps, on va chercher à trier le plus rapidement possible sans indication.

**Et si on est plusieurs ?**

Un jeu de cartes comprend généralement des couleurs et des numéros.
Est-ce cela peut aider à aller plus vite ?

Méthode systématique de tri
---------------------------

Et si maintenant, il faut trier cinquante mille cartes ?
Comment faudrait-il faire ?
Les exercices suivant peuvent être fait à plusieurs ou seul en
plaçant les cartes à plat sur une table.

.. _s-tribulle:

**remettre de l'ordre**

On distribue aux enfants une ou deux cartes (selon le nombre d'enfants ou et de cartes).
On suppose qu'on sait dire si deux cartes sont dans le bon ordre ou pas si on
les présente de gauche à droite.
Les enfants sont placés en ligne et ne peuvent échanger qu'avec leurs deux voisins.
Chaque enfant a une position dans la ligne.
La règle est simple : pour deux enfants voisins,
l'enfant plus proches du début - donc le plus à gauche - doit échanger ses
cartes avec ses voisins si elles ne sont pas dans le bon ordre.

.. image:: tri1.png

Ce tri correspond au `tri à bulles <http://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles>`_.
Pourquoi à votre avis ?

Une illustration de ce tri sous Scratch est
décrite au paragraphe :ref:`l-prog_tri`.

**construire un arbre pour trier**

On remet à tous les enfants sauf un  une carte et deux fils de laine : un rouge, un bleu.

* Le premier enfant choisi aléatoirement se place au milieu de la pièce.
* Le second enfant compare sa carte avec le premier. Si sa carte est
  plus petite, il s'accroche au fil rouge. Si elle est plus grande, il
  s'accroche au fil bleu.
* Le troisième enfant compare sa carte au premier. Si elle est plus petite,
  il s'accroche au fil rouge, si le fil rouge est déjà pris, il compare sa carte
  à celle de l'enfant au bout du fil. Il s'accroche dès qu'il trouve une place libre.

.. image:: tri2.png

Il existe une façon pour le dernier enfant de ramasser simplement
toutes les cartes dans le bon ordre. Saurez-vous la trouver ?

Il s'agit dans ce dernier cas du `tri par arbre <http://rmdiscala.developpez.com/cours/LesChapitres.html/Cours4/TArbrechap4.6.htm>`_.

**couper, trier, fusionner**

Lorsqu'on est plusieurs ou qu'on doit trier un grand nombre de cartes,
il est plus simple de trier des petits bouts puis de les assembler.

Comment regrouper deux jeux de cartes triés pour ne former qu'un seul
paquet qui soit trié également ? Il faut trouver la méthode la plus efficace.

Ordre alphabétique
------------------

Connaissez-vous l'ordre alphabétique ?

Comment cherche-t-on un mot dans un dictionnaire ?

Est-ce que cela serait plus simple si les mots n'étaient pas triés ?

Combien ouvre-t-on de pages avant de trouver son mot ?

Solution
--------

Voir :ref:`l-algo_tri_sol`.

A quoi ça sert ?
----------------

On se sert souvent du tri, surtout que tout est trié.
A la bibliothèque, tout semble bien ordonné.
Les papiers administratif sont rangés par date, les devoirs
sont triés par notes, les mots du dictionnaire sont triés
sinon il serait quasiment impossible de les retrouver.
Le tri sert à retrouver facilement les choses triées.

Citez autour de vous des *choses* qui sont triées. On a vu le dictionnaire. Y en a-t-il d'autres ?

Dans une gare ?

Dans des livres ?

Dans votre téléphone ?

Dans votre cuisine ?

Et le linge ?

Connaissez-vous le tableau de Mendeleïev ?
