#!/usr/bin/env python3

"""
    euler7.py
    2020
"""

import numpy as np

def sieve(n):
    """ Sieve of Erathostenes using numpy"""
    primes = np.ones(n, dtype=bool)
    primes[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i::i] = False
    return np.nonzero(primes)[0]

print(sieve(200_000)[10_000])
# 104743
