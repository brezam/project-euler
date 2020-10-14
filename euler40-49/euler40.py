#!/usr/bin/env python3

"""
    euler40.py
    2020
"""

product = 1

for target_digit in (1, 10, 100, 1_000, 10_000, 100_000, 1_000_000):
    current_digit = 0
    for n in range(1, target_digit):
        final_digit = current_digit + len(str(n))
        if final_digit >= target_digit:
            answer = str(n)[target_digit - current_digit - 1]
            product *= int(answer)
            break
        current_digit = final_digit

print(product)
# 210
