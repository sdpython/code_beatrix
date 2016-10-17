"""
@file
@brief  shortcut to data
"""
import os


def load_prenoms_w():
    """
    returns a list of first names,
    taken from `Nominis <http://nominis.cef.fr/contenus/prenom/alphabetique.html>`_.
    """
    folder = os.path.abspath(os.path.dirname(__file__))
    name = os.path.join(folder, "prenoms_w.txt")
    with open(name, "r", encoding="utf-8") as f:
        names = f.readlines()
    names = [_.strip(" \n\r\t") for _ in names]
    return [_ for _ in names if _]
