# -*- coding: utf-8 -*-
"""
@file
@brief Function solving the TSP problem
"""

import random


def distance_point(p1, p2):
    """
    Returns the Euclidian distance between two points.
    Retourne la distance euclidienne entre deux points.

    @param      p1      point 1
    @param      p2      point 2
    @return             distance
    """
    d = 0
    for a, b in zip(p1, p2):
        d += (a - b) ** 2
    return d ** 0.5


def distance_circuit(points):
    """
    Computes the distance of this circuit.
    Calcule la longueur d'un circuit.

    @param      points      list of points, the circuit assumes they are giving in that order
    @return                 distance
    """
    d = 0
    for i in range(1, len(points)):
        d += distance_point(points[i - 1], points[i])
    return d + distance_point(points[0], points[-1])


def permutation(points, i, j):
    """
    Switches two points and returns a new path.
    Echange deux points et retourne le nouveau circuit.

    @param      points      circuit
    @param      i           first index
    @param      j           second index (< len(points))
    @return                 new circuit
    """
    points = points.copy()
    points[i], points[j] = points[j], points[i]
    return points


def reverse(points, i, j):
    """
    Reverses a sub part of circuit.
    Retourne une partie du circuit.

    @param      points      circuit
    @param      i           first index
    @param      j           second index (<= len(points))
    @return                 new circuit
    """
    points = points.copy()
    if i > j:
        i, j = j, i
    c = points[i:j]
    c.reverse()
    points[i:j] = c
    return points


def voyageur_commerce_simple(points):
    """
    Solves the TSP using basic permutations,
    points are 2D coordinates.
    Résoud le problème du voyageur de commerce.

    @param      points      list of points
    """
    d0 = distance_circuit(points)
    dnew = d0
    n = len(points) - 1
    first = True
    while dnew < d0 or first:
        first = False
        d0 = dnew

        # first pass : random
        for i in range(len(points)):
            h1 = random.randint(0, n)
            h2 = random.randint(0, n)
            p = permutation(points, h1, h2)
            d = distance_circuit(p)
            if d < dnew:
                dnew = d
                points = p

            h1 = random.randint(0, n)
            h2 = random.randint(h1 + 1, n + 1)
            p = reverse(points, h1, h2)
            d = distance_circuit(p)
            if d < dnew:
                dnew = d
                points = p

        # second pass : no reverse
        for i in range(len(points)):
            for j in range(i + 1, len(points) + 1):
                p = reverse(points, i, j)
                d = distance_circuit(p)
                if d < dnew:
                    dnew = d
                    points = p

    return points


def plot_circuit(points, ax=None, **kwargs):
    """
    Plots the circuit on a graph.
    Dessine la solution du voyageur de commerce.

    @param      points      points
    @param      ax          axe
    @param      kwargs      sent to ``plt.subplots``
    @return                 ax
    """
    if ax is None:
        import matplotlib.pyplot as plt
        _, ax = plt.subplots(**kwargs)

    ax.plot([_[0] for _ in points], [_[1] for _ in points], "o")

    p2 = points + [points[0]]
    ax.plot([_[0] for _ in p2], [_[1] for _ in p2], "-")
    return ax
