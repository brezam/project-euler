#!/usr/bin/env python3

"""
    euler3.py
    2020
"""


def factorize(number):
    factors = []
    while number > 1:
        for i in range(2, int(number**.5) + 1):
            if number % i == 0:
                factors.append(i)
                number //= i
                break
        else:
            factors.append(number)
            return factors


print(max(factorize(600851475143)))
# 6857
