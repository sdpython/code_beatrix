
.. issue.

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

C'est l'algorithme `glouton <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos#Algorithme_glouton>`_.

Solution
--------

Voir :ref:`l-algo_sacados_sol`.


A quoi ça sert ?
----------------

Comment rentrez-vous les valises quand vous partez en vacances ou quand vous
déménagez ? Par quelle valise commencez-vous ?

