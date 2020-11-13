#!/usr/bin/env python3

"""
    euler52.py
    2020
"""


from collections import Counter


def same_digits(number, multiples):
    num_digits = Counter(str(number))
    return all(
        Counter(str(number * mul)) == num_digits
        for mul in multiples
    )


print(next((i for i in range(1, 1_000_000) if same_digits(i, (2,3,4,5,6))), None))
# 142857
