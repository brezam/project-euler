#!/usr/bin/env python3

"""
    euler4.py
    2020
"""

def is_palindrome(number):
    return str(number) == str(number)[::-1]

print(max(i*j for i in range(999, 0, -1) for j in range(i, 0, -1) if is_palindrome(i*j)))
# 906609
