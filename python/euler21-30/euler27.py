#!/usr/bin/env python3

"""
    euler27.py
    2020
"""

def is_prime(n: int) -> bool:
    ''' 6k+-1 primality test '''
    if n < 4:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i and n % (i + 2) for i in range(5, int(n**.5)+1, 6))


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
