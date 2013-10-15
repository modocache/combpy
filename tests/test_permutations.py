#-*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest

from combpy.permutations import derangements


def test_derangements_with_2_elements():
    assert set(derangements(["one", "two"])) == set([("two", "one")])

def test_derangements_with_3_elements():
    assert set(derangements([1, 2, 3])) == set([(2, 3, 1), (3, 1, 2)])

def test_derangements_of_uniterable_raises():
    with pytest.raises(TypeError):
        [d for d in derangements(None)]

def test_derangements_of_underangeable_is_empty():
    assert set(derangements([1])) == set()

def test_derangements_of_empty_is_not_empty():
    # Lists of 0 objects vacuously satisfy the derangement
    # condition that no object appears in its original position.
    assert set(derangements([])) == set([()])

