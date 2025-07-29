def strsort(word):
    list_word = sorted(word)
    word_sorted = "".join(list_word)
    return word_sorted

print(strsort("cba"))