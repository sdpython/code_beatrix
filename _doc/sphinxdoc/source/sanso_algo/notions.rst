
.. issue.

.. _l-algo_sans_ordinateur_notions:




.. index:: notion, concept

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
Comment l'attaquer ? Il faut une stratégie pour le résoudre, 
un plan de bataille. Il faut le couper en petits bouts
et chercher une solution pour chacun de ses bouts.

Les informaticiens aiment aussi beaucoup le terme 
`heuristique <http://fr.wikipedia.org/wiki/Heuristique_%28math%C3%A9matiques%29>`_.
C'est une sorte de règle dont on sait qu'elle marche bien pour un problème donné.


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

**Algorithme optimal**


On parle d'*algorithme optimal* pour un problème données 
lorsque celui-ci produit une solution et qu'il n'est pas
possible de produire cette même solution plus rapidement.

On parle de *solution optimale* à un problème lorsqu'il n'existe pas de meilleure
solution à ce problème.

Pour la grande majorité de problème, on sait écrire un algorithme
qui calcule la solution optimale. Mais ce n'est pas forcément
l'algorithme optimal. On ne sait pas toujours dire si un algorithme
est optimal. Dans la grande majorité, on fabrique des *algorithmes
rapides* qui produisent des *solutions approchées* mais tout-à-fait satsifaisante.


    
**Concept clés d'un algorithme**

* **La séquence** - on effectue des tâches les unes à la suite des autres.
* **Le choix** - on fait telle ou telle chose selon une certaine condition.
* **La répétition** - on recommence jusqu'à ce qu'on ait fini (mais entre-temps le résultat final se construit petit à petit).
  On parle aussi de **boucles**.
* **Variables** - pour mémoriser l'état de l'algorithme.
* **Données** - les données que manipule l'algorithme (les nombres qu'il trie, ...)
* **Résultats** - quelque chose à partir des données.
* **Coût** - ou sa vitesse, le coût d'un algorithme est le nombre d'opérations
  élémentaires nécessaires pour qu'il se termine (une opération numérique,
  la consultation d'une variable, un test...) On le calcule rarement
  précisément mais on veur toujours avoir un ordre de grandeur :
  si mon problème est dix fois plus grand, l'algorithme
  sera combien sera combien de fois plus lent ?
  

Par exemple, le tri le plus rapide est en :math:`O(n \log n)`
où :math:`n` est le nombre d'éléments à trier.
La fonction :math:`\log(n)` ou `logarithme <http://fr.wikipedia.org/wiki/Logarithme>`_
détermine le nombre de fois qu'il a fallu multiplier 10 pour obtenir :math:`n`.
Par exemple, :math:`1000=10*10*10` donc :math:`\log(1000)=3`.

Donc, pour trier :math:`n=100` éléments, il faut environ
:math:`100 \log(100) = 100 * 2 = 200`. Pour trier 10 fois plus
d'éléments, il faut : :math:`1000 \log(1000) = 3000`.
Trier 1000 éléments est 15 fois plus lent que trier 100 éléments.


**Vocabulaire**

Voir :ref:`l-glossary`.


