"""
basic checking
"""


def check_chute():
    """
    basic checkings
    """
    dirname = os.path.dirname(__file__)
    f0 = os.path.exists(dirname, "chute.sb2")
    if not os.path.exists(f0):
        raise FileNotFoundError(f0)