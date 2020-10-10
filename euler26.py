#!/usr/bin/env python3

"""
    euler26.py
    2020
"""


def expansion(number, divisor, max_tries=10_000):
    """ returns digits of euclidian divison and 
        whether it has recurring digits or not 
    """
    digits = []
    while number < divisor:
        number *= 10
    seen = [number]
    for _ in range(max_tries):
        div, rem = divmod(number, divisor)
        digits.append(div)
        number = rem * 10
        try:
            idx = seen.index(number)
            return digits[idx:], True
        except ValueError:
            pass
        if number <= 1:
            return digits, False
        seen.append(number)

best_length = 0
best_number = None
for d in range(1, 1_000):
    digits, is_recurring = expansion(1, d)
    if is_recurring and len(digits) > best_length:
        best_number = d
        best_length = len(digits)

print(best_number)
# 983
