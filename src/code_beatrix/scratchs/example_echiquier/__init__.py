"""
@file
@brief basic checking
"""
import os


def check_echiquier():
    """
    basic checkings
    """
    dirname = os.path.dirname(__file__)
    f1 = os.path.join(dirname, "echiquier.sb2")
    if not os.path.exists(f1):
        raise FileNotFoundError(f1)
    f0 = os.path.join(dirname, "echiquier0.sb2")
    if not os.path.exists(f0):
        raise FileNotFoundError(f0)
