#!/usr/bin/env python3

"""
    euler45.py
    2020
"""

def generate_numbers(formula: callable, ceiling: int):
    n = 0
    while True:
        n += 1
        number = formula(n)
        if number >= ceiling:
            break
        yield number

ceiling = 1_600_000_000 # trial and error

pentagonal = set(generate_numbers(lambda n: n * (3 * n - 1) // 2, ceiling))
hexagonal = set(generate_numbers(lambda n: n * (2 * n - 1), ceiling))

for n, number in enumerate(generate_numbers(lambda n: n * (n + 1) // 2, ceiling), 1):
    if number in pentagonal and number in hexagonal:
        print(f"T({n}) = P({n}) = H({n}) = {number}")
# T(1) = P(1) = H(1) = 1
# T(285) = P(285) = H(285) = 40755
# T(55385) = P(55385) = H(55385) = 1533776805
