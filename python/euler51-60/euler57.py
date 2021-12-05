#!/usr/bin/env python3

"""
    euler57.py
    2020
"""


from fractions import Fraction


count = 0
numbers = []
for digit in (1 if i == 0 else 2 for i in range(1001)):
    numbers.append(digit)
    rev_numbers = reversed(numbers)
    d = Fraction(next(rev_numbers), 1)
    for digit in rev_numbers:
        d = 1 / d + digit
    num = d.numerator
    den = d.denominator
    if len(str(num)) > len(str(den)):
        count += 1

print(count)
# 153
