lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

nueva_lista = [num1*num2 for num1,num2 in zip(lista1,lista2)]
print(nueva_lista)