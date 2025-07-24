def pl_sentence(sentence):
    final_sentence = []
    #list_words = sentence.split(" ")

    for word in sentence.split(" "):
        if word[0] in 'aeiou':
            final_sentence.append(f"{word}way")
        else:
            final_sentence.append(f"{word[1:]}{word[0]}ay")

    return " ".join(final_sentence)

print(pl_sentence('this is a test translation'))