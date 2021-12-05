#!/usr/bin/env python3

"""
    euler53.py
    2020
"""


from scipy.special import binom


def lru_cache(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


lru_binom = lru_cache(binom)

count = 0
for n in range(1, 101):
    for r in range(n + 1):
        res = lru_binom(n, min(r, n - r))
        if res > 1_000_000:
            count += 1

print(count)
# 4075
