#!/usr/bin/env python3

"""
    euler36.py
    2020
"""

def is_palindrome(number):
    return str(number) == str(number)[::-1]

total = sum(n for n in range(1_000_000) if is_palindrome(n) and is_palindrome(f"{n:b}"))

print(total)
# 872187
