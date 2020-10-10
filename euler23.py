#!/usr/bin/env python3

"""
    euler23.py
    2020
"""

from functools import lru_cache


LIMIT = 28123

@lru_cache(maxsize=LIMIT)
def is_abundant(number):
    total = 1
    for div in range(2, int(number**.5) + 1):
        if number%div == 0:
            other = number // div
            total += div
            if div != other:
                total += other
            if total > number:
                return True
    return False

total = 0
for number in range(1, LIMIT + 1):
    for n1 in range(number // 2 + 1):
        n2 = number - n1
        if (is_abundant(n1) and is_abundant(n2)):
            break
    else:
        total += number

print(total)
# 4179871
