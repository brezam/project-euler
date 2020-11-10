#!/usr/bin/env python3

"""
    euler2.py
    2020
"""


def fib(up_to):
    a, b = 0, 1
    while b < up_to:
        yield b
        a, b = b, b+a


print(sum(n for n in fib(4e6) if n%2==0))
# 4613732
