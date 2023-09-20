# Operación de descifrado

# Matriz a descifrar
cifrated_matrix_parners = np.array([
  [1, 0, 2, 4],
  [10, 16, 2, 15],
  [26, 17, 16, 7]
])

print("Matriz a descifrar")
print(cifrated_matrix_parners)

# Llave de cifrado cruda
Key = np.array([
    [4, 3, 1],
    [2, 2, 1],
    [1, 1, 1]
])
print("Llave de cifrado cruda")
print(Key)

# Llave invertida modulo 27
keyDescifred = np.linalg.inv(Key) % 27
print("Llave invertida modulo 27")
print(keyDescifred)

# Producto interno llave descifrada por matriz crifrada
product = np.dot(keyDescifred, cifred_matrix)
print("Producto interno llave descifrada por matriz crifrada")
print(product)

# Aplicamos módulo y transponemos matriz
descifrate_matrix = (product % 27).T
print("Aplicamos módulo y transponemos matriz")
print(descifrate_matrix)

# Desciframos código
print("Matriz a texto")
print(matrix_to_text(descifrate_matrix))