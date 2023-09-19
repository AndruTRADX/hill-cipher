# Operación de cifrado

# Matriz a cifrar
matrix = text_to_matrix(textv1)
matrix_np = np.array(matrix)

# Transponemos matriz
matrix_np_t = matrix_np.T

# Llave de cifrado cruda
key = np.array([
    [4, 3, 1],
    [2, 2, 1],
    [1, 1, 1]
])

# Producto interno llave cruda y matriz transpuesta
product = np.dot(key, matrix_np_t)

# Aplicamos módulo y obtenemos matriz transpuesta
cifred_matrix = product % 27
print(cifred_matrix)