#!/usr/bin/env python3

"""
    euler33.py
    2020
"""

from math import gcd
from functools import reduce


def simplify_fraction(num, dem):
    gcd_ = gcd(num, dem)
    return num//gcd_, dem//gcd_


def obtained_by_canceling(num, dem):
    """ Returns fractions obtained by cancelling common digits in numerator
    and denominator.
    """
    str_num = str(num)
    str_dem = str(dem)
    common_digits = (d for d in str_num if d in str_dem)
    result = []
    for digit in common_digits:
        new_num = list(str_num)
        new_num.remove(digit)
        new_dem = list(str_dem)
        new_dem.remove(digit)
        if new_dem != ['0']:
            result.append((int(''.join(new_num)), int(''.join(new_dem))))
    return result


curious_fractions = set()
for dem in range(11, 100):
    for num in range(10, dem):
        if '0' in str(num) and '0' in str(dem):
            continue # We don't want trivial examples

        for num2, dem2 in obtained_by_canceling(num, dem):
            if num2 / dem2 == num / dem:
                curious_fractions.add((num, dem))

product = reduce(lambda f1, f2: (f1[0]*f2[0], f1[1]*f2[1]), curious_fractions)
print(simplify_fraction(*product))
# (1, 100)
