#!/usr/bin/env python3

"""
    euler50.py
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


def best_consecutive_sum(prime_array: np.ndarray):
    setprimes = set(prime_array)
    maxprime = prime_array[-1]
    cumsum = prime_array.cumsum()
    for length in range(prime_array.size, 0, -1):
        for i in range(0, prime_array.size - length):
            total = cumsum[i+length] - cumsum[i]
            if total > maxprime:
                break
            if total in setprimes:
                return total, length


print(best_consecutive_sum(sieve(1_000_000)))
# (997651, 543)
