"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    rounds = [number, number + 1, number + 2]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    total = rounds_1 + rounds_2
    return total


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False


def card_average(hand):
    avg = sum(hand)/len(hand)
    return avg


def approx_average_is_average(hand):
    avg = sum(hand)/len(hand)
    first_last_avg = (hand[0] + hand[-1])/2
    median_avg = hand[len(hand)//2]
    if avg in (first_last_avg,median_avg):
        return True
    return False


def average_even_is_average_odd(hand):
    even = []
    odd = []
    for index,card in enumerate(hand):
        if index % 2 == 0:
            even.append(card)
        odd.append(card)
    print(even)
    print(odd)
    avg_even = sum(even)/len(even)
    avg_odd = sum(odd)/len(odd)
    if avg_even == avg_odd:
        return True
    return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand