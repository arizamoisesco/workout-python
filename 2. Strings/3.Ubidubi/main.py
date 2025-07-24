def ubbi_dubbi(word):
    list_letter = []

    for letter in word:
        if letter in 'aeiou':
            #list_letter.append("ub"+letter)
            list_letter.append(f"ub{letter}")
        else:
            list_letter.append(letter)
    
    return "".join(list_letter)

print(ubbi_dubbi("elephant"))