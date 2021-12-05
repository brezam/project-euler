#!/usr/bin/env python3

"""
    euler38.py
    2020
Since n > 1 the number must have
5 digits or less
"""


STR_DIGITS_1_TO_9 = set('123456789')

best = 0
for num in range(98765, 0, -1):
    if len(set(str(num))) != len(str(num)):
        continue
    max_multiple = 2
    while True:
        concatenated = int(''.join(
            str(num*m) for m in range(1, max_multiple+1)
        ))
        if concatenated > 987654321:
            break
        if set(str(concatenated)) == STR_DIGITS_1_TO_9 and concatenated > best:
            best = concatenated
        max_multiple += 1

print(best)
# 932718654
