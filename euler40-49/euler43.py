#!/usr/bin/env python3

"""
    euler43.py
    2020
"""

from itertools import permutations

total = 0
for perm in permutations("0123456789"):
    if perm[0] == "0":
        continue
    if all(int(''.join(perm[i:i+3])) % p == 0
        for i, p in zip(range(1, 10), (2, 3, 5, 7, 11, 13, 17))
    ):
        total += int(''.join(perm))

print(total)
# 16695334890
