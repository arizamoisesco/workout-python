from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

#1. Esta función determina el número de repeticiones que hay por CADA palabra una a la vez
def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


#Esta función toma la lista de palabras y determina cual es la más grande usando la función anterior
def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)

print(most_repeating_word(WORDS))