"""
@file
@brief Position in a classroom
"""

import random
from pyquickhelper.loghelper import noLOG
from .data import load_prenoms_w


def plot_positions(positions, edges=None, ax=None, **options):
    """
    draw positions and first names into a graph

    @param      positions       list of 3-uple (name, x, y)
    @param      ax              axis
    @param      edges           edges
    @param      options         options for matplotlib
    @return                     ax

    First position: 0
    """
    from matplotlib.patches import Rectangle

    if ax is None:
        import matplotlib.pyplot as plt
        _, ax = plt.subplots(
            nrows=1, ncols=1, figsize=options.get('figsize', (5, 5)))

    if isinstance(positions, dict):
        positions = [(k,) + v for k, v in positions.items()]
    maxx = -1
    maxy = -1
    for name, x, y in positions:
        r = Rectangle((x - 0.45, y - 0.45), 0.9, 0.9,
                      fill=(0, 0, 255), alpha=0.5)
        ax.add_patch(r)
        ax.text(x * 1.0, y * 1.0, name,
                verticalalignment='center', horizontalalignment='center',
                fontsize=options.get('fontsize', 15),
                color=options.get('color_text', (0, 0, 0)))
        maxx = max(x, maxx)
        maxy = max(y, maxy)
    if edges is not None:
        posdict = {k: (x, y) for k, x, y in positions}
        if isinstance(edges, list):
            for e1, e2 in edges:
                p1 = posdict[e1]
                p2 = posdict[e2]
                if p1 != p2:
                    dx = ((p2[0] - p1[0]) / abs(p2[0] - p1[0])
                          * 0.1) if p2[0] != p1[0] else 0.0
                    dy = ((p2[1] - p1[1]) / abs(p2[1] - p1[1])
                          * 0.1) if p2[1] != p1[1] else 0.0
                    d = distance(p1, p2)
                    if d < 1.1:
                        color = "y"
                    elif d < 1.9:
                        color = "b"
                    else:
                        color = "r"
                    ax.arrow(p1[0] + dx, p1[1] + dy,
                             p2[0] - p1[0] - dx, p2[1] - p1[1] - dy,
                             color=color, shape="full",
                             head_width=0.05, head_length=0.1, lw=3)
        else:
            raise TypeError("edges should be list")
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


def distance(p1, p2):
    """
    computes the distance between two positions

    @param      p1      position 1
    @param      p2      position 2
    @return             distance
    """
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def measure_positions(positions, edges):
    """
    returns the sum of edges weights

    @param      positions       dictionary ``{ name : (x, y) }``
    @param      edges           list of affinities ``(name1, name2)``
    @return                     distance
    """
    if isinstance(edges, list):
        s = 0
        for name1, name2 in edges:
            s += distance(positions[name1], positions[name2])
        return s
    else:
        s = 0
        for name, names in edges.items():
            s += sum(distance(positions[name], positions[o]) for o in names)
        return s / 2.0


def find_best_positions_greedy(positions, edges, name):
    """
    find the best position for name, explore all positions

    @param      positions       dictionary ``{ name : (x, y) }``
    @param      edges           list of affinities as a dictionary ``{ name: [names] }``
    @param      name            name to optimize
    @return                     list of positions
    """
    if not isinstance(edges, dict):
        raise TypeError("edges must be dict")
    if name not in edges:
        # nothing to do
        return None
    else:
        d0 = measure_positions(positions, edges)
        deltas = []
        p0 = positions[name]
        for na, pos in positions.items():
            c = positions.copy()
            p = positions[na]
            c[na] = p0
            c[name] = p
            dall = measure_positions(c, edges) - d0
            deltas.append((dall, pos))

        deltas.sort()
        return deltas


def optimize_positions(positions, edges, max_iter=100, fLOG=noLOG,
                       plot_folder=None):
    """
    optimize the positions

    @param      positions       dictionary ``{ name : (x, y) }``
    @param      edges           list of affinities ``(name1, name2)``
    @param      max_iter        maximum number of iterations
    @return                     positions, iterations
    """
    edges_dict = {}
    for name1, name2 in edges:
        if name1 in edges_dict:
            edges_dict[name1].append(name2)
        else:
            edges_dict[name1] = [name2]
        if name2 in edges_dict:
            edges_dict[name2].append(name1)
        else:
            edges_dict[name2] = [name1]
    edges_dict = {k: set(v) for k, v in edges_dict.items()}

    fLOG("[optimize_positions] #edges=%d #edges_dict=%d" %
         (len(edges), len(edges_dict)))

    if isinstance(positions, list):
        positions = {k: (x, y) for k, x, y in positions}

    def find_name(positions, edges_dict):
        keys = list(sorted(positions.keys()))
        name = keys[random.randint(0, len(keys) - 1)]
        while name not in edges_dict:
            name = keys[random.randint(0, len(keys) - 1)]
        return name

    list_positions = {pos: 0 for _, pos in positions.items()}
    for k, v in positions.items():
        list_positions[v] += 1
    if max(list_positions.values()) > 1:
        raise ValueError("duplicated position:\n{0}".format(
            str({k: v for k, v in list_positions.items() if v > 1})))

    name = find_name(positions, edges_dict)
    fLOG("[optimize_positions] name='%s' pos=%s" %
         (name, str(positions[name])))
    total = measure_positions(positions, edges)
    iter = 0
    memo = [(total, name, positions[name])]
    while iter < max_iter:

        if plot_folder is not None:
            import os
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
            plot_positions(positions, edges=edges, ax=ax)
            img = os.path.join(plot_folder, "classroom_%04d.png" % iter)
            fig.savefig(img)
            plt.close('all')

        deltas = find_best_positions_greedy(positions, edges_dict, name)
        delta, new_pos = deltas[0]
        if new_pos == positions[name] or delta >= 0:
            # no change, we put the name in the empty spot
            name = None
        else:
            rev = {v: k for k, v in positions.items() if k != name}
            current_name = rev[new_pos]
            fLOG("[optimize_positions] iter=%d total=%1.3f name='%s' <--> '%s' delta=%1.3f new_pos=%s" %
                 (iter, total, name, current_name, delta, str(new_pos)))

            # we switch
            old_pos = positions[name]
            positions[name] = new_pos
            positions[current_name] = old_pos

            # next name
            name = current_name
            if name not in edges_dict:
                name = None
            else:
                list_positions = {pos: 0 for _, pos in positions.items()}
                for k, v in positions.items():
                    list_positions[v] += 1
                sup = {k: v for k, v in list_positions.items() if v > 1}

        if name is None:
            name = find_name(positions, edges_dict)
            if name is None:
                raise ValueError("impossible")

        total = measure_positions(positions, edges)
        memo.append((total, name, positions[name]))

        iter += 1

    # final check
    list_positions = {pos: 0 for _, pos in positions.items()}
    for k, v in positions.items():
        list_positions[v] += 1
    sup = {k: v for k, v in list_positions.items() if v > 1}
    if len(sup) > 0:
        raise ValueError(
            "Too many first names at the same positions: {0}".format(sup))
    return positions, memo
