"""
basic checking
"""


def check_pyramide():
    """
    basic checkings
    """
    dirname = os.path.dirname(__file__)
    f1 = os.path.exists(dirname, "pyramide.sb2")
    if not os.path.exists(f1):
        raise FileNotFoundError(f1)
    f0 = os.path.exists(dirname, "pyramide0.sb2")
    if not os.path.exists(f0):
        raise FileNotFoundError(f0)
