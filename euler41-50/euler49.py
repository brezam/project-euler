#!/usr/bin/env python3

"""
    euler49.py
    2020
"""

import itertools


def is_prime(n):
    return (n > 1 and
        (n % 2 or n == 2) and
        all(n%d != 0 for d in range(3, int(n**.5)+1, 2))
    )


def permutation_triple(permutations):
    ''' Returns permutations that obey arithmetic sequence '''
    for combination in itertools.combinations(permutations, 3):
        nums = [int(''.join(digits)) for digits in combination]
        a, b, c = sorted(nums)
        if b-a == c-b != 0:
            yield a, b, c

for four_digits_comb in itertools.combinations_with_replacement('0123456789', r=4):

    permutations = itertools.permutations(four_digits_comb)

    four_digit_unique_perms = set(
        triad for triad in permutations if all(triad[i][0] != "0" for i in range(3))
    )

    for triple in permutation_triple(four_digit_unique_perms):
        if all(is_prime(number) for number in triple):
            print(f"{triple} --> {''.join(''.join(str(n)) for n in triple)}")

# (1487, 4817, 8147) --> 148748178147
# (2969, 6299, 9629) --> 296962999629
