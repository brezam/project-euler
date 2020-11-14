#!/usr/bin/env python3

"""
    euler28.py
    2020
"""

INDEX_OFFSET = {'down': (+1, 0), 'left': (0, -1), 'up': (-1, 0), 'right': (0, +1)}
TO_THE_RIGHT = {'down': 'left', 'left': 'up', 'up': 'right', 'right': 'down'}


def next_indices_and_direction(i, j, direction, table):
    y, x = INDEX_OFFSET[TO_THE_RIGHT[direction]]
    if table[i+y][j+x] is None:
        direction = TO_THE_RIGHT[direction]
    final_y, final_x = INDEX_OFFSET[direction]
    if not (0 <= i+final_y < len(table) and 0 <= j+final_x < len(table)):
        return None
    return i+final_y, j+final_x, direction


def sum_diagonals(table):
    return sum(
        element
        for i, row in enumerate(table)
        for j, element in enumerate(row)
        if i == j or j == len(row) - 1 - i
    )

size = 1001
table = [[None]*size for _ in range(size)]


table[size//2][size//2] = 1
direction = 'right'

i, j = size//2, size//2 + 1
number = 1
while True:
    number += 1
    table[i][j] = number
    values = next_indices_and_direction(i, j, direction, table)
    if values is None:
        break
    i, j, direction = values

print(sum_diagonals(table))
# 669171001
