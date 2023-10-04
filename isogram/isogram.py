def is_isogram(string):
    freq = {}
    string_1 = string.replace(' ','')
    string_2 = string_1.replace('-','')
    new_string = string_2.lower()
    for letter in new_string:
        if letter in freq:
            return False
        freq[letter] = 1
    return True