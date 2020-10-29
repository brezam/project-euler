#!/usr/bin/env python3

"""
    euler12.py
    2020
"""

def count_divisors(number):
    return sum(2 for div in range(1, int(number**.5)+1) if number%div==0) - (number%2==0)

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
