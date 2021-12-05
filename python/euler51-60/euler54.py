#!/usr/bin/env python3

"""
    euler54.py
    2020
"""


from collections import Counter


CARD_VALUE = dict(zip("23456789TJQKA", range(2, 15)))


def sorted_cards(cards):
    return sorted(cards, key=lambda x: CARD_VALUE[x[0]])


def royal_flush(cards):
    sorted_ = sorted_cards(cards)
    suit = sorted_[0][1]
    return all(c[0] == r and c[1] == suit for c, r in zip(sorted_, "TJQKA"))


def straight_flush(cards):
    sorted_ = sorted_cards(cards)
    suit = sorted_[0][1]
    return all(
        CARD_VALUE[b[0]] - CARD_VALUE[a[0]] == 1 and b == suit
        for a, b in zip(sorted_, sorted_[1:])
    )


def four_of_a_kind(cards):
    values = Counter(c[0] for c in cards)
    return next((k for k, v in values.items() if v == 4), False)


def full_house(cards):
    values = Counter(c[0] for c in cards)
    if 3 not in values and 2 not in values:
        return False
    triplet = next(k for k, v in values.items() if v == 3)
    double = next(k for k, v in values.items() if v == 2)
    return triplet, double


def flush(cards):
    suit = cards[0][1]
    return all(c[1] == suit for c in cards)


def straight(cards):
    sorted_ = sorted_cards(cards)
    suit = sorted_[0][1]
    return all(
        CARD_VALUE[b[0]] - CARD_VALUE[a[0]] == 1 for a, b in zip(sorted_, sorted_[1:])
    )


def three_of_a_kind(cards):
    values = Counter(c[0] for c in cards)
    return next((k for k, v in values.items() if v == 3), False)


def two_pairs(cards):
    values = Counter(c[0] for c in cards)
    pairs = [k for k, v in values.items() if v == 2]
    if len(pairs) < 2:
        return False
    return max(cards, key=lambda x: CARD_VALUE[x[0]])[0]


def one_pair(cards):
    values = Counter(c[0] for c in cards)
    return next((k for k, v in values.items() if v == 2), False)


def high_card(cards):
    return max(cards, key=lambda x: CARD_VALUE[x[0]])[0]


def select_winner(p1_cards, p2_cards, ordered_rank_functions):
    for rank in ordered_rank_functions:
        p1 = rank(p1_cards)
        p2 = rank(p2_cards)
        if not p1 and p2:
            return "p2"
        if p1 and not p2:
            return "p1"
        if CARD_VALUE.get(p1, 0) > CARD_VALUE.get(p2, 0):
            return "p1"
        if CARD_VALUE.get(p1, 0) < CARD_VALUE.get(p2, 0):
            return "p2"
    return "tie"


def main():
    games = []
    with open("p054_poker.txt") as f:
        for line in f:
            cards = line.rstrip().split(" ")
            games.append((cards[:5], cards[5:]))

    priorities = [
        royal_flush,
        straight_flush,
        four_of_a_kind,
        full_house,
        flush,
        straight,
        three_of_a_kind,
        two_pairs,
        one_pair,
        high_card,
    ]
    p1_wins = 0
    for game in games:
        p1, p2 = game
        winner = select_winner(p1, p2, priorities)
        if winner == 'p1':
            p1_wins += 1

    print(p1_wins)
    # 376

if __name__ == "__main__":
    main()
