num = 0
cant = 0
lista = []
sigue = True
print("Finalize con el numero 0.")
while (sigue):
    num = int(input("Introduzca un numero: "))
    if (num != 0):
        cant +=1
        lista.append(num)
    else:
        sigue = False

orden = True
for i in range(len(lista) - 1):
    if (lista[i] > lista[i + 1]):
        orden = False
        break

if (orden == True):
    print(f"Genial, la lista esta en orden y contiene {cant} elementos!")
else:
    print(f":( La lista no esta ordenada y contiene {cant} elementos.")


