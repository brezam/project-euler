#!/usr/bin/env python3

"""
    euler17.py
    2020
"""

ones = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

def number_length(n):
    if n < 20:
        return len(ones[n])
    elif n < 100:
        return len(tens[n // 10]) + len(ones[n % 10])
    hundreds = (n // 100) % 10
    thousands = n // 1000
    left = n % 100

    result = 0
    if n > 999:
        result += number_length(thousands) + len("thousand")
    if hundreds:
        result += number_length(hundreds) + len("hundred")
    if left:
        result += len("and") + number_length(left)
    return result

print(sum(number_length(n) for n in range(1, 1001)))
# 21124
