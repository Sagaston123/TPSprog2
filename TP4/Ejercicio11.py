from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999, 3, 2, 1, 251]
mayor = reduce(lambda x, y: x if x>y else y, lista)
print(mayor)

