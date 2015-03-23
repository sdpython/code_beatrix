"""
Exercice à propos du parcours d'un échiquier.
"""


def check():
    """
    vérifie que certains fichiers sont ici
    """
    dirname = os.path.dirname(__file__)
    f1 = os.path.exists(dirname, "echiquier.sb2")
    if not os.path.exists(f1):
        raise FileNotFoundError(f1)
    f0 = os.path.exists(dirname, "echiquier0.sb2")
    if not os.path.exists(f0):
        raise FileNotFoundError(f0)
