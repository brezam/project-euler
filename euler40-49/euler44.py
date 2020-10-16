#!/usr/bin/env python3

"""
    euler44.py
    2020
"""


from collections import namedtuple


def pentagon_gen(ceiling):
    n = number = 1
    while number < ceiling:
        yield number
        n += 1
        number = n*(3*n-1) // 2


def main():
    ceiling = 10_000_000
    pentagon_nums = list(pentagon_gen(ceiling))
    pentagon_set = set(pentagon_nums)

    Best = namedtuple("Best", "D j k")
    best = Best(float('inf'), 0, 0)

    for j in range(len(pentagon_nums)-1):
        P_j = pentagon_nums[j]
        for k in range(j+1, len(pentagon_nums)):
            P_k = pentagon_nums[k]
            if P_j + P_k > ceiling: 
                break
            if (
                P_j + P_k in pentagon_set and 
                P_k - P_j in pentagon_set and
                P_k - P_j < best.D
            ):
                best = Best(P_k - P_j, j, k)
    print(best)
    # Best(D=5482660, j=1019, k=2166)


if __name__ == "__main__":
    main()
