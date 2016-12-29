
.. blogpost::
    :title: La programmation avec les cartes
    :keywords: enseignement, cours, ENSAE
    :date: 2015-09-05
    :categories: cours

    J'avais décidé de reprendre quelques-uns des jeux développés pour les enfants
    lors de mon premier cours à l'ENSAE.
    On a passé un peu de temps à déployer un fil de laine
    au milieu de l'amphithéâtre
    pour illustrer un algortihme.
    On a joué avec des cartes.
    Il y eut quelques fou rires aussi.

    .. suite.

    Le travail lors des deux heures qui suivirent fut
    plus studieux mais j'ai repris les cartes pour expliquer
    quelques bouts de code utilisant les listes.
    Alors que j'avais insisté sur la distinction entre la position
    d'un élément d'une liste et sa valeur, les élèves tombaient sur cet
    exemple qui mélangeaient allègrement les deux ::

        l = [ 4, 3, 0, 2, 1 ]
        i = 0
        while l[i] != 0 :
            i = l[i]
            print (i)  # que vaut l[i] à la fin ?

    J'ai donc repris les cartes je disposai comme suit :

    .. image:: carte1.jpg
        :width: 600

    Il n'y avait pas de carte zéro dans mon jeu donc j'ai pris une image
    ronde qui la symbolise.
    Les cartes sont disposées en ligne, de la position **0** à la position **4** car
    en Python, la première case est la position 0. Pour connaître
    la valeur de l'élément du tableau, on retourne la carte.
    Le jeu est simple :

    * Pour obtenir l'élément *i* du tableau, on compte à partir du début
      à partir de 0 jusqu'à *i*.
    * Pour connaître l'élément du tableau, on retourne la carte.

    .. image:: carte2.jpg
        :width: 600

    Puis on suit l'algorithme, tant que la carte retournée
    n'est pas zéro (ou le bus dans notre cas), on à la position indiquée par la
    carte retournée donc 4 :

    .. image:: carte3.jpg
        :width: 600

    Puis carte 1 (soit la deuxième en partant de la gauche) :

    .. image:: carte4.jpg
        :width: 600

    Puis 3 :

    .. image:: carte5.jpg
        :width: 600

    Puis 2 :

    .. image:: carte6.jpg
        :width: 600

    Et on a trouvé.

    Pour la petite note, cet algorithme sert à déterminer les
    `cycles d'une permutation <https://fr.wikipedia.org/wiki/Permutation#D.C3.A9composition_en_produit_de_cycles_.C3.A0_supports_disjoints>`_.
