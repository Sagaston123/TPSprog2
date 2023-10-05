lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cuadrado(lista):
    lista_nueva = [elem**2 for elem in lista_original]
    return lista_nueva

print(cuadrado(lista_original))
