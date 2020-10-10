#!/usr/bin/env python3

"""
    euler5.py
    2020
"""

import math
from functools import reduce

def _lcm(x, y):
    return abs(x*y) // math.gcd(x, y)

def lcm(*args):
    return reduce(_lcm, args)

print(lcm(*range(1, 21)))
# 232792560
