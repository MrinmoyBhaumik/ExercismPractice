def add_prefix_un(word):
    new_word = "un" + word
    return new_word


def make_word_groups(vocab_words):
    string = " :: " + vocab_words[0]
    return string.join(vocab_words)
        
        


def remove_suffix_ness(word):
    return word[:-4]


def adjective_to_verb(sentence, index):
    return sentence.split()[index] + "en"
