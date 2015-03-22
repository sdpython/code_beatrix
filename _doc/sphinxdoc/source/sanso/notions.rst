
.. issue.

.. _l-algo_sans_ordinateur_notions:





Notions, Concepts
=================



**Stratégies**

Il n'existe pas toujours de solution parfaite ou de solution parfaite
qui puisse être mise en oeuvre en un temps raisonnable.
Une solution est souvent un assemblage de briques.
Certains reviennent plus souvent que d'autres comme
trier les éléments, procéder par 
`récurrence <http://fr.wikipedia.org/wiki/D%C3%A9finition_par_r%C3%A9currence>`_
(ajouter de nouveaux éléments un par un en adaptant la meilleure solution).

On a utilise parfois un langage guerrier quand on parle d'un problème.
Comment l'attaquer ? Il faut stratégie pour le résoudre, 
un plan de bataille. Il faut le couper en petits bouts
et chercher une solution pour chacun de ses bouts.


**Propriété locale - globale**


C'est une façon de découper une problème. Une solution à
un problème n'est pas toujours facile à comprendre dans son 
ensemble mais elle est plus facile à interpréter localement.

Lorsqu'un ensemble d'objets est trié, cela veut dire que si on prendre
deux éléments rangés côte à côte, ils sont toujours dans le bon ordre.
Une idée pour trier des éléments est de faire respecter cette propriété locale :
et d'inverser deux éléments proches qui sont mal rangés. 
C'est l'idée du `tri à bulles <http://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles>`_
qui permet effectivement d'obtenir un tableau trié.

    
**Concept clés d'un algorithme**

* **La séquence** - on effectue des tâches les unes à la suite des autres.
* **Le choix** - on fait telle ou telle chose selon une certaine condition.
* **La répétition** - on recommence jusqu'à ce qu'on ait fini (mais entre-temps le résultat final se construit petit à petit).
* **Variables** - pour mémoriser l'état de l'algorithme.
* **Données** - les données que manipule l'algorithme (les nombres qu'il trie, ...)
* **Résultats** - quelque chose à partir des données.

**Vocabulaire**

Voir :ref:`glossary`.


