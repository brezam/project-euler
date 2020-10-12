#!/usr/bin/env python3

"""
    euler39.py
    2020
"""

from collections import namedtuple

BestP = namedtuple("BestP", "p length")

best = BestP(0, 0)

for p in range(3, 1001):
    length = 0
    for c in range(p - 3, p // 3, -1):
        for b in range(p - c - 1, p // 3 - 1, -1):
            a = p - b - c
            if a < 1:
                continue
            if a * a + b * b == c * c:
                length += 1
    if length > best.length:
        best = BestP(p, length)

print(best)
# BestP(p=840, length=7)
