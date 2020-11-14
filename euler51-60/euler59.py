#!/usr/bin/env python3

"""
    euler59.py
    2020
"""


from itertools import product


with open("p059_cipher.txt") as f:
    message = [int(n) for n in f.read().split(",")]


def message_score(decrypted):
    score = 0
    for char in decrypted:
        if ord("a") <= ord(char) <= ord("z") or ord("A") <= ord(char) <= ord("Z"):
            score += 1
    return score


best_text = ""
best_score = 0
for key in product(range(ord("a"), ord("z") + 1), repeat=3):
    decrypted = ""
    for i, value in enumerate(message):
        decrypted += chr(value ^ key[i % 3])
    if message_score(decrypted) > best_score:
        best_text = decrypted
        best_score = message_score(decrypted)

print(sum(ord(x) for x in best_text))
# 129448
