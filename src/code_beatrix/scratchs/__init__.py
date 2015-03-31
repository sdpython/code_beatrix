"""
shortcuts for scratch
"""

#from .example_echiquier import check as check1

from .example_echiquier import check_echiquier
from .example_tri import check_tri


def check():
    """
    run checking functions
    """
    check_echiquier()
    check_tri()
