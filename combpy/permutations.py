#-*- coding: utf-8 -*-

from __future__ import absolute_import

import itertools

from combpy.factorials import subfactorial


def permutations(iterable, r = None):
    return itertools.permutations(iterable, r)


def derangements(iterable):
    """
    Yields derangements of *iterable*, where derangements
    are permutations in which none of the objects in the
    original list appear in their original place. For example,

    >>> set(derangements([1, 2, 3]))
    set([(2, 3, 1), (3, 2, 1)])
    """

    if len(iterable) == 1:
        return

    for permutation in permutations(iterable):
        is_derangement = True

        for index, element in enumerate(permutation):
            if element == iterable[index]:
                is_derangement = False
                break

        if is_derangement:
            yield permutation


def number_of_derangements(iterable):
    return subfactorial(len(iterable))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

