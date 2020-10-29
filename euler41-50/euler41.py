#!/usr/bin/env python3

"""
    euler41.py
    2020
"""

from itertools import permutations


def is_prime(num):
    return (
        num > 1
        and (num % 2 != 0 or num == 2)
        and all(num % div != 0 for div in range(3, int(num ** 0.5) + 1, 2))
    )


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
