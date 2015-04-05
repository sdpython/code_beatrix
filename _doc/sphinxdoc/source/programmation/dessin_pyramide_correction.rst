
.. issue.

.. index:: solution, dessin, pyramide, scratch, programmation

.. _l-prog_dessin_pyramide_sol:

Construire une pyramide de balles (solution)
============================================



**Q1 :** 

Il est plus facile de commencer par le haut et de fait grandir la pyramide
jusqu'en bas. De cette façon, on peut créer des pyramides aussi grandes qu'on veut.
Dans l'autre sens, la taille de la base détermine la taille finale de la pyramide
avant qu'on l'ait terminée.


**Q2 :** 

D'après la question précédente, il est préférable de commencer par le haut.
La premier balle porte le numéro 1 et est celle du haut. Ensuite,
un continue la numérotation en parcourant chaque ligne.

.. image:: pyramide_num.png

De cette façon, on peut toujours agrandir la pyramide.
Ce n'est pas le cas si on part vers le bas pour numéroter.

**Q3 :** 

Le numéro de chaque balle n'indique pas sur quelle ligne elle se
trouve. On va s'en changer cela.

.. image:: pyramide_num2.png


**Q4 :** 

Lorsqu'on regarde la seconde numérotation de chaque balle, on s'aperçoit
que le premier numéro indique la ligne, le second la position de la balle
sur cette ligne. Le problème est que ces deux nombres simples n'ont aucun
rapport avec la position de la balle dans l'écran de Scratch. 
C'est pour cela qu'on fait la distinction entre la numérotation à deux chiffres
de la balle et ses coordonnées sur l'écran de Scratch.
Si on note :math:`x_0` et :math:`y_0`, on obtient comme relation entre les deux :

.. math::
    
    x = x_0 + j * sx + i * sx/2 
    
    y = y_0 - i * sy 


Passer d'un système de numérotation (donc des coordonnées) au système
de coordonnées de l'écran n'est pas toujours évident.


Exercice 1
----------

L'astuce est de remarquer que, sur la ligne 1, il y a une balle,
sur la ligne 2, il y a deux balles, et ainsi de suite :
sur la ligne *i*, il y *i* balles.

La solution est illustrée par :

.. image:: pyramide_solution.png

Et le programme à exécuter est le suivant :
:download:`echiquier.sb2 <../../../../src/code_beatrix/scratchs/example_echiquier/echiquier.sb2>`.
    

