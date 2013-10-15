#-*- coding: utf-8 -*-

from math import factorial, floor


def subfactorial(n):
    return floor(factorial(n) *
        sum([((-1)**k)/float(factorial(k)) for k in range(n+1)]))

