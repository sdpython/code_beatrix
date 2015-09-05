

.. index:: parti

.. _l-algo_division:


Le parti divisé
===============


A partir de 7-8 ans (mais ce n'est qu'une indication).


Dans un certain pays, il existe un parti politique pétri d'inimitiés tenaces. 
Est-il possible de scinder le parti en deux pour que chaque paire d'ennemis 
intangibles se retrouve de part et d'autre du fossé ?


Mise en scène
-------------

On remplit des bouteilles d'eau (une dizaine) qu'on dispose un peu n'importe comment dans une salle.
On relie certaines d'entre elles par une ficelle rouge. Chaque ficelle rouge symbolise deux personnes
qui ne s'apprécient pas. Il faut dire à chaque nouvelle ficelle si on peut 
divisier les bouteilles en deux groupes de telles sortes que deux bouteilles
reliées par une ficelle soient chacun dans un groupe différent. Pour ce faire, 
on peut utiliser une ficelle de couleur verte pour symboliser par frontière
entre les deux groupes.

L'objectif est de trouver à quelle condition sur les ficelles rouges 
on peut couper le groupe de bouteilles en deux.


Quelques indices :

**Q1 :** On considère le groupe de bouteilles suivant avec quelques ficelles rouges.
         On voit clairement deux groupes de bouteilles ! A-t-on besoin de savoir 
         comment un groupe est divisé pour diviser l'autre ?

.. image:: parti1.png

**Q2 :** Que se passe-t-il lorsque trois bouteilles sont reliés entre elles ?

A vous.

**Q3 :** Et quand il y a plus de trois bouteilles ?


Autres options à programmer
---------------------------

.. index:: composante connexe, graphe

Les aspects algorithmiques abordés ici sont très proches du concept
de `composante connexe <https://fr.wikipedia.org/wiki/Graphe_connexe>`_ dans un graphe.
Le *graphe* est ici composé de l'ensemble des bouteilles et des arcs. Le graphe le plus connu
est Facebook où les bouteilles sont les personnes et les ficelles sont des connexions.

Une composante connexe est un groupe de bouteilles qui sont reliées par des ficelles : 
on peut passer d'une bouteille (ou noeud du graphe)
à n'importe quelle autre du groupe en suivant les ficelles (ou arc du graphe).

**Q4 :** combien y a-t-il de composantes connexes dans cet ensemble de bouteilles ?

.. image:: parti2.png



Solution
--------

Voir :ref:`l-algo_division_sol`.


A quoi ça sert ?
----------------

.. index:: coloriage


Sans le savoir, trouver les composantes connexes dans un graphe revient à colorier
le graphe. On choisit une bouteille et on la colorie en rouge. On suit toutes les ficelles
qui la relient à d'autres et on colorie ces autres de la même couleur. 

.. image:: parti3.png

**Q5 :** On fait quoi ensuite ?




.. [#fdiv1] Ce problème est tiré d'une compétition google code jam : 
            `Bad Horse <https://code.google.com/codejam/contest/6234486/dashboard#s=p0>`_
            
