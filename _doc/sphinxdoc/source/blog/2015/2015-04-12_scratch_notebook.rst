

.. blogpost::
    :title: Scratch dans un notebook
    :keywords: scratch, notebook, ipython, javascript
    :date: 2015-04-12
    :categories: scratch, notebook
    
    Je me suis demandé s'il était possible d'inclure
    facilement des projets Scratch dans le site web.
    Etant donné qu'il est généré à l'aide de 
    `Sphinx <http://sphinx-doc.org/>`_, cela revenait à se demander
    s'il existe une version Javascript de 
    `Scratch <https://scratch.mit.edu/>`_.
    Celle-ci s'appelle `Snap! <http://snap.berkeley.edu/snapsource/snap.html>`_.
    Je suis tombé ensuite sur cette page 
    `How-To: Control a PoppyCreature using the visual programming language Snap! (a variant of Scratch) <http://nbviewer.ipython.org/github/poppy-project/pypot/blob/master/samples/notebooks/Controlling%20a%20Poppy%20Creature%20using%20SNAP.ipynb>`_
    qui donne quelques liens sur comment se dépatouiller avec Snap.
    Un peu plus loin
    l'astuce décrite dans l'article 
    `More about interactive graphs using Python, d3.js, R, shiny, IPython, vincent, d3py, python-nvd3 <http://www.xavierdupre.fr/blog/2013-11-30_nojs.html>`_
    m'a permis de construire le notebook suivant :
    :ref:`scratchdansunnotebookrst`.
    
    Il me reste à convertir les fichiers d'extensions ``.sb2`` que
    Scratch utilise pour sauver ses projets mais j'ai bon
    espoir d'y arriver avec 
    `Snapin8r <https://github.com/Hardmath123/Snapin8r>`_.
    
    A quoi ça sert... à pouvoir jouer avec les solutions
    sans même avoir à installer quoi que ce soit et automatiser
    le tout.
    