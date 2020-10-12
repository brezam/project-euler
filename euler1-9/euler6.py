#!/usr/bin/env python3

"""
    euler6.py
    2020
"""

def sum_of_squares(range_):
    return sum(d*d for d in range_)

def square_of_sum(range_):
    return sum(range_)**2

print(square_of_sum(range(1,101)) - sum_of_squares(range(1,101)))
# 25164150
