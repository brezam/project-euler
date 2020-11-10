#!/usr/bin/env python3

"""
    euler21.py
    2020
"""


def sum_divisors(number):
    return sum(num for div in range(1, int(number**.5)+1) 
                if number%div==0 
                for num in {div, number//div}
                if num != number)


seen = set()
numbers = []
for number in range(1, 10_000):
    other_number = sum_divisors(number)
    if (
        other_number != number
        and other_number not in seen
        and sum_divisors(other_number) == number
    ):
        numbers.extend((number, other_number))
        seen.update({number, other_number})

print(sum(numbers))
# 31626
