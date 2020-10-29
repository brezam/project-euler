#!/usr/bin/env python3

"""
    euler37.py
    2020
"""

import numpy as np


UPPER_BOUND = 1_000_000 # ?


def sieve(n):
    """ Sieve of Erathostenes using numpy"""
    primes = np.ones(n, dtype=bool)
    primes[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i::i] = False
    return np.nonzero(primes)[0]


def truncates(number):
    str_number = str(number)
    return ({int(str_number[:n]) for n in range(1, len(str_number))} |
           {int(str_number[n:]) for n in range(len(str_number))})


primes = set(sieve(UPPER_BOUND))

total = 0
for n in range(10, UPPER_BOUND):
    if n in primes and all(m in primes for m in truncates(n)):
        total += n

print(total)
# 748317
