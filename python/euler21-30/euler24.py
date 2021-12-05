#!/usr/bin/env python3

"""
    euler24.py
    2020
"""

from itertools import permutations, islice

perm = permutations("0123456789")

print(''.join(next(islice(perm, 1_000_000-1, 1_000_000))))
# 2783915460
