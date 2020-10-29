#!/usr/bin/env python3

"""
    euler9.py
    2020
"""

for c in range(1000, 0, -1):
    for b in range(1000-c, (1000-c)//2-1, -1):
        a = 1000-c-b
        if a*a + b * b == c * c:
            print(a*b*c)
# 31875000
