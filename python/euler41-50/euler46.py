#!/usr/bin/env python3

"""
    euler46.py
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


def problem46(prime_cache):
    setprimes = set(primes)
    n = 3
    while True:
        if n not in setprimes:
            for prime in prime_cache:
                if prime >= n:
                    return n
                sqrt = round(((n - prime)//2)**.5)
                if 2*sqrt*sqrt == (n - prime):
                    #print(f"{n} = {prime} + 2 x {sqrt}^2")
                    break
        n += 2

primes = sieve(1_000_000).tolist()
smallest_odd_composite = problem46(primes)
print(smallest_odd_composite)
# 5777
