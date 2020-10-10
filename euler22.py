#!/usr/bin/env python3

"""
    euler22.py
    2020
"""

def name_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)


with open("p022_names.txt") as f:
    data = sorted(name.strip("\"") for name in f.read().split(","))

total = sum(index*name_value(name) for index, name in enumerate(data, 1))

print(total)
# 871198282
