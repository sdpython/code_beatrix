"""
@file
@brief basic checking
"""
import os


def check_pyramide():
    """
    basic checkings
    """
    dirname = os.path.dirname(__file__)
    f1 = os.path.join(dirname, "pyramide.sb2")
    if not os.path.exists(f1):
        raise FileNotFoundError(f1)
    f0 = os.path.join(dirname, "pyramide0.sb2")
    if not os.path.exists(f0):
        raise FileNotFoundError(f0)
    f2 = os.path.join(dirname, "pyramide_bio.sb2")
    if not os.path.exists(f2):
        raise FileNotFoundError(f2)
