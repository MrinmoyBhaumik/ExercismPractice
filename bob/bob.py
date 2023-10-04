def response(hey_bob):
    if hey_bob.isspace() or hey_bob == '':
        return 'Fine. Be that way!'
    if  (hey_bob.rstrip())[-1] == '?' and hey_bob.isupper():
        return 'Calm down, I know what I\'m doing!'
    if (hey_bob.rstrip())[-1] == '?' and hey_bob != '':
        return 'Sure.'
    if hey_bob.isupper() and any(letter.isalpha() for letter in hey_bob):
        return 'Whoa, chill out!'
    return 'Whatever.'
