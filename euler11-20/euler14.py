#!/usr/bin/env python3

"""
    euler14.py
    2020
"""

def collatz_steps(number):
    steps = 0
    while number > 1:
        number = 3*number + 1 if number%2 else number//2
        steps += 1
    return steps

no_steps, number = max((collatz_steps(i), i) for i in range(10**6))
print(number)
# 837799
