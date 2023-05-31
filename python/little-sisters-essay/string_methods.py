"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    title_list = list(title)
    title_list[0] = title[0].upper()
    for index,i in enumerate(title_list):
        if i == ' ':
            title_list[index+1] = title_list[index+1].upper()
    new_title = "".join(title_list)
    return new_title


def check_sentence_ending(sentence):
    if sentence[-1] == '.':
        return True
    return False


def clean_up_spacing(sentence):
    new_sentence = sentence.strip()
    return new_sentence


def replace_word_choice(sentence, old_word, new_word):
    new_sentence = sentence.replace(old_word,new_word)
    return new_sentence