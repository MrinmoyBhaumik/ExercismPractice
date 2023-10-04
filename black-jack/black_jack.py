"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ("J" , "K" , "Q"):
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one,card_two)
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    if (card_one == 'A') or (card_two == 'A'):
        return 1
    if value_of_card(card_one) + value_of_card(card_two) < 11:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    if (card_one == 'A' and value_of_card(card_two) == 10) or (card_two == 'A' and value_of_card(card_one) == 10) or (value_of_card(card_one) + value_of_card(card_two)==21):
        return True
    return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    if (value_of_card(card_one) + value_of_card(card_two) == 9) or (value_of_card(card_one) + value_of_card(card_two) == 10) or (value_of_card(card_one) + value_of_card(card_two) == 11):
        return True
    return False