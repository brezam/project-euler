#!/usr/bin/env python3

"""
    euler55.py
    2020
"""


def palindrome_after_iterations(number, max_iterations=50):
    iterations = 0
    str_n = str(number)
    rev_str_n = str_n[::-1]
    for _ in range(max_iterations):
        str_n = str(int(str_n) + int(rev_str_n))
        rev_str_n = str_n[::-1]
        iterations += 1
        if str_n == rev_str_n:
            break
    else:
        return None
    return iterations


total = sum(1 for n in range(1, 10_000) if palindrome_after_iterations(n) is None)
print(total)
# 249
