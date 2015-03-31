"""
basic checking
"""

def check_tri():
    """
    basic checkings
    """
    dirname = os.path.dirname(__file__)
    f1 = os.path.exists(dirname, "bubble_sort.sb2")
    if not os.path.exists(f1):
        raise FileNotFoundError(f1)
