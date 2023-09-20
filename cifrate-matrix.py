# Operación de cifrado

# Matriz a cifrar
matrix = text_to_matrix(textv1)

matrix_np = np.array(matrix)

# Transponemos matriz
matrix_np_t = matrix_np.T
print("Transponemos matriz")
print(matrix_np_t)

# Llave de cifrado cruda
key = np.array([
    [4, 3, 1],
    [2, 2, 1],
    [1, 1, 1]
])
print("Llave de cifrado cruda")
print(key)

# Producto interno llave cruda y matriz transpuesta
product = np.dot(key, matrix_np_t)
print("Producto interno (Multiplicación) llave cruda y matriz transpuesta")
print(product)

# Aplicamos módulo y obtenemos matriz transpuesta
cifred_matrix = product % 27
print("Aplicamos módulo y obtenemos matriz transpuesta")
print(cifred_matrix)
print(matrix_to_text(cifred_matrix))