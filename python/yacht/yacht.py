# Score categories.
# Change the values as you see fit.
YACHT = 'Yacht'
ONES = 'Ones'
TWOS = 'Twos'
THREES = 'Threes'
FOURS = 'Fours'
FIVES = 'Fives'
SIXES = 'Sixes'
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = 'Four Of A Kind'
LITTLE_STRAIGHT = 'Little Straight'
BIG_STRAIGHT = 'Big Straight'
CHOICE = 'Choice'


def score(dice, category):
    score = 0
    dice_set = set(dice)
    three = 0
    three_num = 0
    two = 0
    two_num = 0
    four = 0
    four_num = 0
    if dice.count(1) >= 1 and category == 'Ones':
        score += dice.count(1)
    if dice.count(2) >= 1 and category == "Twos":
        score += 2*dice.count(2)
    if dice.count(3) >= 1 and category == "Threes":
        score += 3*dice.count(3)
    if dice.count(4) >= 1 and category == "Fours":
        score += 4*dice.count(4)
    if dice.count(5) >= 1 and category == "Fives":
        score += 5*dice.count(5)
    if dice.count(6) >= 1 and category == "Sixes":
        score += 6*dice.count(6)
    for num in dice_set:
        if dice.count(num) == 3:
            three += 1
            three_num += num
        if dice.count(num) == 2:
            two += 1
            two_num += num
        if dice.count(num) >= 4:
            four += 1
            four_num += num
    if three == 1 and two == 1 and category == "Full House":
        score += (3*three_num) + (2*two_num)
    if four == 1 and category == "Four Of A Kind":
        score += 4*four_num
    if min(dice_set) == 1 and max(dice_set) == 5 and len(dice_set) == 5 and category == "Little Straight":
        score += 30
    if min(dice_set) == 2 and max(dice_set) == 6 and len(dice_set) == 5 and category == "Big Straight":
        score += 30
    if category == "Choice":
        score += sum(dice)
    if len(dice_set) == 1 and category == "Yacht":
        score += 50
    return score


