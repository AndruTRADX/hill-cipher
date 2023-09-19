import numpy as np

# Matriz a cadena de texto
def matrix_to_text(matrix):
    letters = "abcdefghijklmnopqrstuvwxyz_"
    planed_matrix = matrix.flatten()
    text_matrix = ""

    for num in planed_matrix:
      text_matrix += letters[(int(num))]

    return text_matrix