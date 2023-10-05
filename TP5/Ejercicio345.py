import random
from functools import reduce

long1 = 0
long2 = 0
lista1 = []
lista2 = []
lista1impares = []
def longitud():
    long1 = random.randint(20, 50)
    long2 = random.randint(20, 50)
    lista1 = [random.randint(200, 5000) for x in range(long1)]
    lista2 = [random.randint(200, 5000) for x in range(long2)]
    return lista1, lista2

lista1impares = []
def impares(lista):
    lista1impares = [i for i in lista if i % 2 != 0]
    return lista1impares

lista1, lista2 = longitud() #Asignacion de contendio aleatorio a las listas
menorL2 = reduce(lambda x, y: x if x<y else y, lista2)  #Encuentra el menor de la lista2
lista1impares = impares(lista1) #Asignacion de contenido de los impares de lista1
lista1imparesM = [i * menorL2 for i in lista1impares]    #Multiplico los valores de la lista1impares por el menor de la lista2

def es_primo(numero):
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def menor_primo_en_lista(lista):
    primos = [num for num in lista if es_primo(num)]
    return primos

primos = menor_primo_en_lista(lista2)   #lista con todos los primos de la lista2
primo_menor = reduce(lambda x, y: x if x<y else y, primos)  #primo_menor es el menor primo de la lista primos

print("La lista 1 es: ", lista1, "\n")
print("----------------------------------------------\n")
print("La lista 2 es: ", lista2, "\n")
print("----------------------------------------------\n")
print("Los impares de la lista 1 son: ", lista1impares, "\n")
print("----------------------------------------------\n")
print("El menor de la lista 2 es: ", menorL2, "\n")
print("----------------------------------------------\n")
print("La lista de los impares multiplicada por el menor de la lista 2 es: ", lista1imparesM, "\n")
print("----------------------------------------------\n")
print("La lista de los todos los primos de L2 es: ", primos, "\n")
print("----------------------------------------------\n")
print("El primo menor de esa lista es: ", primo_menor)
print("----------------------------------------------\n")
