#!/usr/bin/env python3

"""
    euler47.py
    2020
"""


def factorize(number):
    factors = []
    while number:
        i = 2
        while i*i <= number:
            if number % i == 0:
                factors.append(i)
                number //= i
                break
            i += 1 if i == 2 else 2
        else:
            if number != 1:
                factors.append(number)
            return factors


number_in_a_row = 4
n = 1
while n < 1_000_000:
    for m in range(number_in_a_row):
        factors = set(factorize(n+m))
        if len(factors) != number_in_a_row:
            n += m + 1
            break
    else:
        print(*range(n, n+number_in_a_row))
        break

# 134043 134044 134045 134046
