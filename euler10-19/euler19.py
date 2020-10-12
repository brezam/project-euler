#!/usr/bin/env python3

"""
    euler19.py
    2020
"""

from datetime import date, timedelta


start = date(1901, 1, 1)
end = date(2000, 12, 13)

day = start
while day.weekday() != 6:
    day += timedelta(days=1)
sunday = day

count = 0
while sunday <= end:
    if sunday.day == 1:
        count += 1
    sunday += timedelta(days=7)

print(count)
# 171
