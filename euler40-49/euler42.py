#!/usr/bin/env python3

"""
    euler42.py
    2020
"""

from string import ascii_uppercase



def word_value(word, char_value):
    return sum(char_value[char] for char in word)


def triangle_numbers_generator(ceiling):
    number = index = 1
    while number < ceiling:
        yield number
        number = index * (index + 1) // 2
        index += 1

def main():
    char_value = dict(zip(ascii_uppercase, range(1, 27)))
    words = []
    with open('p042_words.txt') as f:
        words = [word.strip("\"") for word in f.read().split(',')]

    longest_word_length = max(len(w) for w in words)
    ceiling = longest_word_length*26
    triangle_nums = set(triangle_numbers_generator(ceiling))

    count = sum(1 for word in words if word_value(word, char_value) in triangle_nums)
    print(count)
    # 162

if __name__ == "__main__":
    main()
