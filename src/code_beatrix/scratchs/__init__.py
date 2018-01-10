"""
@file
@brief shortcuts for scratch
"""

#from .example_echiquier import check as check1

from .example_echiquier import check_echiquier
from .example_tri import check_tri
from .example_pyramide import check_pyramide
from .example_chute import check_chute


def check():
    """
    run checking functions
    """
    check_echiquier()
    check_tri()
    check_pyramide()
    check_chute()
    return True
