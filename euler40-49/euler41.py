#!/usr/bin/env python3

"""
    euler41.py
    2020
"""

from itertools import permutations


def is_prime(n):
    return n > 1 and all(n%d != 0 for d in range(2, int(n**.5) + 1))


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
