#!/usr/bin/env python3

"""
    euler56.py
    2020
"""


def digital_sum(number):
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


best = 0
for a in range(101):
    for b in range(101):
        dig_sum = digital_sum(a ** b)
        best = max(best, dig_sum)

print(best)
# 972
