#!/usr/bin/env python3

"""
    euler35.py
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


def rotations(number):
    str_number = str(number)
    return {int(str_number[i:] + str_number[:i]) for i in range(1, len(str_number))}


primes_under_million = set(sieve(1_000_000))
circular_primes = set()
for n in range(2, 1_000_000):
    if n in primes_under_million:
        rotations_n = rotations(n)
        if all(rot in primes_under_million for rot in rotations_n):
            circular_primes.add(n)
            circular_primes.update(set(rotations_n))

print(len(circular_primes))
# 55
