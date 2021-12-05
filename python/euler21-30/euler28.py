#!/usr/bin/env python3

"""
    euler28.py
    2020
"""


def table_diagonals(size):
    step = number = 1
    diagonals = [1]
    for _ in range(size // 2):
        for _ in range(4):
            number += step + 1
            diagonals.append(number)
        step += 2
    return diagonals


print(sum(table_diagonals(1001)))
# 66917101
