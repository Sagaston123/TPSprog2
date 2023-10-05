num = 0
cant = 0
suma = 0
sigue = True
while (sigue):
    num = int(input("Ingrese un numero entero: "))
    if (num >= 0):
        cant +=1
        suma += num
    else:
        print("El numero que introdujo es negativo, se termina el programa")
        sigue = False

prom = suma / cant
print(f"El promedio es {prom} con un total de {cant} numeros ingresados positivos.")



