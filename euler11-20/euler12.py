#!/usr/bin/env python3

"""
    euler12.py
    2021
"""


def count_divisors(positive):
    if positive < 1: 
        return 0
    sqrt = int(positive ** 0.5)
    step = 2 if positive % 2 else 1
    return sum(2 for div in range(1, int(positive**.5)+1, step) if positive%div==0
    ) - (sqrt*sqrt == positive)


def triangle_numbers(max_idx):
    total = 0
    number = 1
    for _ in range(max_idx):
        total += number
        number += 1
        yield total


for number in triangle_numbers(999_999):
    if count_divisors(number) > 500:
        print(number)
        break

# 76576500
