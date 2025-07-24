def pig_latin():
    word = input("Ingrese su palabra en ingles: ")
    if word[0] in 'aeiou':
        word = word + "way"
    else:
        first_letter = word[0]
        word = word[1:] + first_letter + "ay"

    return word


print(pig_latin())