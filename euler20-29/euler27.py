#!/usr/bin/env python3

"""
    euler27.py
    2020
"""

def is_prime(number):
    return number > 1 and all(number%div != 0 for div in range(2, int(number**.5) + 1))


def quadratic(a, b, n):
    return n*n + a*n + b


best = 0
a_times_b = None
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            if not is_prime(quadratic(a, b, n)):
                break
            n += 1
        if n > best:
            best = n
            a_times_b = a*b

print(a_times_b) 
# -59231
