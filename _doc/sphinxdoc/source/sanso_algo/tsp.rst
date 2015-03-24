
.. issue.

.. _l-algo_tsp:

Le voyageur de commerce
=======================

A partir de 7-8 ans (mais ce n'est qu'une indication).


Le problème du `voyageur de commerce <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_
est un problème très classique en informatique. Imaginez que deviez passer par Dunkerque, Paris, Lyon,
Strasbourg, Marseille, Toulours, Bordeaux, Nantes, Limoges, Dijon, Lilles, Rouen, Reims, Saint-Etienne
pour revenir à Dunkerque. Dans quelle ordre faut-il visiter les villes le plus 
rapidement possible ?


Mise en scène
-------------

On remplit des bouteilles d'eau qu'on dispose un peu n'importe comment dans une salle.
Avec une pelote de laine, on cherche à faire un grand tour pour toutes les relier
puis revenir à celle de départ. 
Le gagnant est celui qui a réussi à relier toutes les bouteilles avec le moins de laine possible.

Par la suite, on pourra simplement numéroter les bouteilles dans le sens
où on doit les parcourir. Le fil servira à mesurer des petits bouts de chemins
et peut-être changer les numéros.

Quelques indices :

**Q1 :** Le bouteille de départ est-elle importante ?

**Q2 :** J'ai relié toutes les bouteilles entre elles et je m'aperçois que les fils se croisent.
Que puis-je faire pour raccourcir le trajet ?

**Q3 :** Il y a deux fils de laines qui suivent presque le même chemin sauf à un endroit :
les deux fils parcourent deux bouteilles consécutives dans un sens différent. Comment s'en servir
sur le reste du chemin ?



Solution
--------

Voir :ref:`l-tsp_sol`.


A quoi ça sert ?
----------------

On ne fait pas souvent le tour de France mais on va souvent au supermarché. 
Quel est le chemin le plus court entre les rayons pour aller acheter tout ce dont on a besoin ?



