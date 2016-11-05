

.. _l-algo_facteur_chinois_sol:


La tournée du camion poubelle (solution)
========================================

Voir `Le postier chinois <http://lesenfantscodaient.fr/notebooks/postier_chinois.html>`_.

La solution est rédigée sous forme de notebook. Les fragments de code servent principalement
pour contruires les illustrations qui émaillent la solution.
Celle-ci commence véritablement au paragraphe *Astuce*.
Ce qui précède décrit numériquement l'exemple choisi
pour ces illustrations. En ce qui concerne les premières
lignes de codes, les trois suivantes 
définissent le style des graphiques et font en sorte que ceux-ci
soient insérées de le notebook.

:: 

    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    %matplotlib inline

Les deux suivantes construisent le menu pour naviguer plus facilement.

::

    from jyquickhelper import add_notebook_menu
    add_notebook_menu()
    
Les deux lignes qui suivent insère une image dans la page.

::

    from pyquickhelper.helpgen import NbImage
    NbImage("7_bridges.png", width="30%")
    
