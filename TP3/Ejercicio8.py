lista = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5 ,6, 7, 8]

nueva_lista = [numero for numero in lista if lista.count(numero) == 1]
print(nueva_lista)