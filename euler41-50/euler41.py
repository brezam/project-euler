#!/usr/bin/env python3

"""
    euler41.py
    2020
"""

from itertools import permutations


def is_prime(n: int) -> bool:
    ''' 6k+-1 primality test '''
    if n < 4:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i and n % (i + 2) for i in range(5, int(n**.5)+1, 6))


for endpoint in range(10, 1, -1):
    pandigitals = (
        int("".join(map(str, perm))) for perm in permutations(range(1, endpoint))
    )
    best_prime = max((n for n in pandigitals if is_prime(n)), default=None)
    if best_prime:
        answer = best_prime
        break

print(answer)
# 7652413
