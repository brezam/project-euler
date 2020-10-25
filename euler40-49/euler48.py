#!/usr/bin/env python3

"""
    euler48.py
    2020
"""

total = 0
for i in range(1, 1001):
    total = (total + i ** i) % 10**10

print(total)
# 9110846700
