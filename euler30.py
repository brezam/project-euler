#!/usr/bin/env python3

"""
    euler30.py
    2020
"""

total = 0
for number in range(10, 6*9**5):
    sum_digit_fifth_power = sum(int(d)**5 for d in str(number))
    if number == sum_digit_fifth_power:
        total += number

print(total)
# 443839
