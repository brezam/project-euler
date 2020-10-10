#!/usr/bin/env python3

"""
    euler25.py
    2020
"""

def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

idx = 0
for i, fib in enumerate(infinite_fibonacci(), 1):
    if len(str(fib)) >= 1_000:
        print(i)
        break
# 4782
