def is_armstrong_number(number):
    num = str(number)
    digits = list(num)
    armstrong = 0
    for digit in digits:
        armstrong += (int(digit)**len(digits))
    if armstrong == number:
        return True
    return False