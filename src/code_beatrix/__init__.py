# -*- coding: utf-8 -*-
"""
@file
@brief Module *code_beatrix*.

.. faqref::
    :title: Pourquoi Python?

    `Python <https://www.python.org/>`_
    est un langage de programmation très répandu aujourd'hui
    qui fut choisi à l'`ENSAE <http://www.ensae.fr/ensae/fr/>`_ en
    2005 pour remplacer le `C++ <https://fr.wikipedia.org/wiki/C%2B%2B>`_.
    Dès la première année, il est apparu que ce nouveau langage permettait
    aux étudiants de mettre leurs idées plus rapidement en forme.
    Les opinions ont commencé alors un peu à changer à propos de la programmation.
    Il est très rare maintenant qu'un étudiant quitte une grande école
    d'ingénieurs sans programmer.
    Il a été choisi pour trois raisons. La première est sa syntaxe
    car il oblige les dévelopeurs à aligner leurs instructions
    ce qui rend les programmes plus lisibles.
    La seconde parce que sa `grammaire <https://docs.python.org/3/reference/grammar.html>`_
    est une des plus courte (voir aussi
    `The Python Language Reference <https://docs.python.org/3/reference/>`_).
    Enfin, beaucoup de librairies existantes mais codées en C++ étaient déjà
    disponibles à l'époque. 10 ans plus tard, le langage est quasi incontournable
    dès qu'on touche au traitement de données.
"""
import os

__version__ = "0.5"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/code_beatrix"
__url__ = "http://lesenfantscodaient/"
__license__ = "MIT License"
__blog__ = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "rss_blog_list.xml"))


def _setup_hook(add_print=False, unit_test=False):
    """
    if this function is added to the module,
    the help automation and unit tests call it first before
    anything goes on as an initialization step.
    It should be run in a separate process.

    @param      add_print       print *Success: _setup_hook*
    @param      unit_test       used only for unit testing purpose
    """
    # we can check many things, needed module
    # any others things before unit tests are started
    if add_print:
        print("Success: _setup_hook")


def check(log=False, kind=None, fLOG=None):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @param      kind    None or ``'scratch'`` or ``'video'``
    @param      fLOG    logging function
    @return             0 or exception
    """
    r = True
    if kind is None or kind == "scratch":
        from .scratchs import check
        r &= check()
    if kind is None or kind == "video":
        from .art.video import check
        r &= check(fLOG=fLOG)
    return r


def load_ipython_extension(ip):
    """
    to allow the call ``%load_ext code_beatrix``

    @param      ip      from ``get_ipython()``
    """
    from .ipythonhelper.magic_scratch import register_scratch_magics
    register_scratch_magics(ip)
