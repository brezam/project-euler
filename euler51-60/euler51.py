#!/usr/bin/env python3

"""
    euler51.py
    2020
"""


import numpy as np
import itertools


def sieve(n):
    """ Sieve of Erathostenes using numpy"""
    primes = np.ones(n, dtype=bool)
    primes[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i::i] = False
    return np.nonzero(primes)[0]


def smallest_prime(prime_list):
    setprimes = set(primes)
    for p in prime_list:
        str_p = str(p)
        for no_digits in range(1, len(str_p)):
            for comb in itertools.combinations(range(len(str_p)), r=no_digits):
                group = []
                if 0 in comb:
                    digits_to_check = '123456789'
                    failure = 1
                else:
                    digits_to_check = '0123456789'
                    failure = 0
                for digit in digits_to_check:
                    new_number = int(''.join(digit if i in comb else d for i, d in enumerate(str_p)))
                    if new_number not in setprimes:
                        failure += 1
                        if failure == 3:
                            break
                    else:
                        group.append(new_number)
                else:
                    return min(group), group


primes = sieve(1_000_000).tolist()
print(smallest_prime(primes))
# (121313, [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393])
