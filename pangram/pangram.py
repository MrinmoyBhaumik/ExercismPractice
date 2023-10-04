def is_pangram(sentence):
    alphabet = set()
    sentence = sentence.lower()
    for letter in sentence:
        if letter not in (' ', '_', '.','"') and letter.isdigit() is not True:
            alphabet.add(letter)
    if len(alphabet) == 26:
        return True
    return False
