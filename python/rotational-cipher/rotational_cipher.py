def rotate(text, key):
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    upper = UPPERCASE[key:] + UPPERCASE[:key]
    lower = LOWERCASE[key:] + LOWERCASE[:key]
    translation = str.maketrans(UPPERCASE + LOWERCASE, upper + lower)
    return text.translate(translation)