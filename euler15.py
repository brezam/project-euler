#!/usr/bin/env python3

"""
    euler15.py
    2020
"""

from math import factorial
from functools import reduce
from operator import mul

def grid_permutations(grid_size):
    no_rights, no_downs = grid_size
    n = no_rights + no_downs
    k = min(no_rights, no_downs)
    return reduce(mul, range(n, n-k, -1), 1) // reduce(mul, range(2, k+1), 1)

print(grid_permutations((20, 20)))
# 137846528820
