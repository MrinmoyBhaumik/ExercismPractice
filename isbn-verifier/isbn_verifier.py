def is_valid(isbn):
    sum = 0
    new_isbn = isbn.replace('-','')
    if len(new_isbn) != 10:
        return False
    for index, char in enumerate(new_isbn):
        if char.isdigit() == False and index != 9:
            return False
        if index == 9 and char.isdigit() == False and char != 'X':
            return False
        if char == 'X' and index == 9:
            sum += 10
        if char.isdigit():
            sum += int(char)*(10-index)
    if sum % 11 == 0:
        return True
    return False