
.. issue.

.. index:: sac-à-dos, solution, poids, algorithme, glouton

.. _l-algo_sacados_sol:

Sac-à-dos (solution)
====================



Il n'existe pas d'algorithme rapide qui permette de trouver la solution optimale 
- la meilleure solution. Mais on peut essayer de trouver une façon rapide
de constuire une solution approchée avec un peu d'astuce.


**Q1 :** 

La pièce la plus difficile à placer dans le sac-à-dos où le coffre d'une voiture
est toujours la plus grosse. C'est pourquoi on commence toujours par elle.
Et puis cela permet de remplir le sac-à-dos rapidement.


**Q2 :** 

La seconde pièce la plus difficle à placer est la seconde pièce la plus lourde. 
Une fois qu'on a placé le premier objet, c'est comme ci on repartait de zéro avec un
sac-à-dos plus petit et une pièce en moins.


**Q3 :** 

Voici la liste d'instructions proposées :

#. Trier les objets par ordre décroissant de poids.
#. Prendre le premier objet de la liste.
#. On essaye de le placer dans le sac-à-dos.
#. S'il tient, on le garde.
#. Qu'il tienne ou pas, on passe à l'objet suivant et on retourne à l'étape 3.

C'est l'algorithme `glouton <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos#Algorithme_glouton>`_
qui est décrit ici. Il en existe plein d'autres pour trouver une solution approchée
à ce problème mais celui-ci est très court, on l'essaye toujours en premier. 

Ensuite, il est vrai, quand on veut vraiment emmener quelque chose en vacances,
on fait tout pour que ça rentre dans le coffre. On fait, on défait mais on enlève rarement
les plus gros sacs du fond du coffre.

Liens
-----

* `Le problème du sac à dos <https://interstices.info/jcms/c_19213/le-probleme-du-sac-a-dos>`_ (interstices.info)


