# Llave de cifrado cruda
Key = np.array([
    [4, 3, 1],
    [2, 2, 1],
    [1, 1, 1]
])

# Llave invertida modulo 27
keyDescifred = np.linalg.inv(Key) % 27
print(Key)

# Producto interno llave descifrada por matriz crifrada
product = np.dot(keyDescifred, cifrated_matrix_parners)

# Aplicamos módulo y transponemos matriz
descifrate_matrix = (product % 27).T
print(descifrate_matrix)

# Desciframos código
print(matrix_to_text(descifrate_matrix))