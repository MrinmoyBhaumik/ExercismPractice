def translate (text):
    text = text.split(" ")
    new_text = []
    for word in text:
        new_text.append(trans(word))
    final_text = " ".join([str(item) for item in new_text])
    return final_text

def trans(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i"or word[0] == "o"or word[0] == "u" or word[0:2]=="yt" or word[0:2]=="xr":
        return (word + "ay")
    if word[0:3] == "thr" or word[0:3] == "sch":
        return (word[3:] + word[0:3] + "ay")
    if word[0:2] == "th" or word[0:2] == "ch" or word[0:2] == "rh":
        return (word[2:] + word[0:2] + "ay")
    if word[0:2]=="qu":
        return (word[2:] + word[0:2] + "ay")
    if (word[0] != "a" or word[0] != "e" or word[0] != "i" or word[0] != "o" or word[0] != "u") and word[1:3]=="qu":
        return (word[3:] + word[0:3] + "ay")
    if word[1] == 'y':
        return (word[1:] + word[0] + "ay")
    if word[2] == 'y':
        return [word[3:] + word[0:3] + "ay"]
    return (word[1:] + word[0] + "ay")


