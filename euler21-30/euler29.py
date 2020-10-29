#!/usr/bin/env python3

"""
    euler29.py
    2020
"""

unique = {a**b for a in range(2, 101) for b in range(2, 101)}

print(len(unique))
# 9183
