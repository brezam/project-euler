#!/usr/bin/env python3

"""
    euler31.py
    2020
"""

"""
Dynamic programming following the table:
                                      0    1   2   3  ...  200
[]                                    -    -   -   -  ...   -
[>1<]                                 -    -   -   -  ...   -
[1, >2<]                              -    -   -   -  ...   -
[1, 2, >5<]                           -    -   -   -  ...   -
   ...                                          ...                 
[1, 2, 5, 10, 20, 50, 100, >200<]     -    -   -   -  ...   !

Let coins be the list of all coins, the value at row col is defined by:
    table[row][col] = table[row-1][col] + table[row][col-coins[row-1]] (Eq. 1)

We want the very last value at bottom-right, which answers how to make
200p (£2) using all the coins. (Note that it's at row len(coins)+1, not len(coins))

We know that we can only make nothing with nothing, so the first row
is [1, 0, 0, ..., 0] (We cannot make 1 with nothing, we cannot make 2 with nothing, etc;
and there's only 1 way to make 0 with nothing.)

Using that fact and (Eq. 1) we can compute the bottom-right value.

PS: All of this was unecessary since using a simpler greedy algorithm is enough for these particular coin set.
"""

def get_value_at(row, col, coins):
    if row < 0 or col < 0 or (row == 0 and col != 0):
        return 0
    if row == 0 and col == 0:
        return 1
    return get_value_at(row-1, col, coins) + get_value_at(row, col - coins[row - 1], coins)


coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200
row = coins.index(target) + 1
col = target
print(get_value_at(row, col, coins))
# 73682
