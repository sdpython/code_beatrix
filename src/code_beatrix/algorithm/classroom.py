"""
@file
@brief Position in a classroom
"""

import random
from .data import load_prenoms_w


def plot_positions(positions, ax=None, **options):
    """
    draw positions and first names into a graph

    @param      positions       list of 3-uple (name, x, y)
    @param      ax              axis
    @param      options         options for matplotlib
    @return                     ax

    First position: 0
    """
    from matplotlib.patches import Rectangle

    if ax is None:
        import matplotlib.pyplot as plt
        _, ax = plt.subplots(
            nrows=1, ncols=1, figsize=options.get('figsize', (5, 5)))

    maxx = -1
    maxy = -1
    for name, x, y in positions:
        r = Rectangle((x - .45, y - 0.45), 0.9, 0.9,
                      fill=(0, 0, 255), alpha=0.5)
        ax.add_patch(r)
        ax.text(x * 1.0, y * 1.0, name,
                verticalalignment='center', horizontalalignment='center',
                fontsize=options.get('fontsize', 15),
                color=options.get('color_text', (0, 0, 0)))
        maxx = max(x, maxx)
        maxy = max(y, maxy)
    ax.set_xlim([-1, maxx + 1])
    ax.set_ylim([-1, maxy + 1])
    return ax


def random_positions(nb, names=None):
    """
    draws random position for some person in a classroom

    @param      nb      number of persons
    @param      names   names (None for default)
    @return             list of 3-uple(name, x, y)
    """
    if names is None:
        names = load_prenoms_w()
        names = names[:nb]

    if nb > len(names):
        raise ValueError("nb={} > len(names)={}".format(nb, len(names)))
    names = names.copy()
    random.shuffle(names)

    nbs = int(nb ** 0.5)
    if nbs != nb**0.5:
        nbs += 1
    positions = []

    ci = 0
    cj = 0
    for name in names:
        positions.append((name, ci, cj))
        cj += 1
        if cj >= nbs:
            ci += 1
            cj = 0
    return positions
