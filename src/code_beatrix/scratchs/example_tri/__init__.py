"""
@file
@brief basic checking
"""
import os


def check_tri():
    """
    basic checkings
    """
    dirname = os.path.dirname(__file__)
    f1 = os.path.join(dirname, "bubble_sort.sb2")
    if not os.path.exists(f1):
        raise FileNotFoundError(f1)
    f2 = os.path.join(dirname, "bubble_sort0.sb2")
    if not os.path.exists(f2):
        raise FileNotFoundError(f2)
