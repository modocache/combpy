#-*- coding: utf-8 -*-

from __future__ import absolute_import

from combpy.factorials import subfactorial


def test_subfactorial():
    assert subfactorial(3) == 2
    assert subfactorial(4) == 9


def test_subfactorial_of_0_is_1():
    assert subfactorial(0) == 1


def test_subfactorial_of_1_is_0():
    assert subfactorial(1) == 0

