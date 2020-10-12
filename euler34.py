#!/usr/bin/env python3

"""
    euler34.py
    2020
"""

from functools import reduce, lru_cache
from operator import mul

@lru_cache(maxsize=2**3)
def factorial(num):
    return reduce(mul, range(2, num+1), 1)

def sum_factorial_digits(num):
    return sum(factorial(int(d)) for d in str(num))

numbers = (n for n in range(10, 7*factorial(9)) if n == sum_factorial_digits(n))
print(sum(numbers))
# 40730
