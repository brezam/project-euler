#!/usr/bin/env python3

"""
    euler58.py
    2020
"""


def is_prime(n: int) -> bool:
    """ 6k+-1 primality test """
    if n < 4:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i and n % (i + 2) for i in range(5, int(n ** 0.5) + 1, 6))


def table_diagonals(max_size):
    step = number = 1
    size = 3
    while size <= max_size:
        group4 = []
        for _ in range(4):
            number += step + 1
            group4.append(number)
        yield size, group4
        step += 2
        size += 2



def main():
    primes = 0
    total = 1  # extra 1 in the middle counts as diagonal
    for size, diag_numbers in table_diagonals(100_000):
        total += 4
        primes += sum(1 for x in diag_numbers if is_prime(x))
        if primes / total < 0.1:
            print(size)
            break


if __name__ == "__main__":
    main()

# 26241
