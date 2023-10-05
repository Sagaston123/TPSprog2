numeros = list(range(1, 101))   #Rango de nuemros

def contar_div(numero):
    divisores = 0
    for x in range (1, numero+1):
        if numero % x == 0:
            divisores += 1
    return divisores

primos = [elem for elem in numeros if contar_div(elem) == 2]
print(primos)
