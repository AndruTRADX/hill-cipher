import numpy as np

# Texto a matriz 3 x n
def text_to_matrix(text):
    vector = []
    matrix = []
    letters = "abcdefghijklmnopqrstuvwxyz_"
    len_iterable = len(text)
    counter = 0

    for letter in text:
        counter += 1

        if letter == '_':
            vector.append(letters.find('_'))
        else:
            vector.append(letters.find(letter.casefold()))

        if counter % 3 == 0 or counter == len_iterable:
            while len(vector) < 3:
                vector.append(letters.find('_'))
            matrix.append(vector)
            vector = []

    return matrix