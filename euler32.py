#!/usr/bin/env python3

"""
    euler32.py
    2020
"""

from itertools import permutations


pandigitals = set()
for sequence in permutations('123456789'):
    for i in range(1, 8):
        for j in range(i+1, 9):
            n1, n2, n3 = sorted(int(''.join(n)) for n in (sequence[:i], sequence[i:j], sequence[j:]))
            if n1*n2 == n3:
                pandigitals.add(n3)

print(sum(pandigitals))
# 45228
