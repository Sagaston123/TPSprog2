vocales = ['a' , 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
palabra = "hola"
def cantvocales(input):
    cant = 0
    for letra in input:
        if letra in vocales:
            cant += 1
    return cant

salir = False
while(not salir):
    print("Si desea terminar, escriba S")
    palabra = input("Ingrese una palabra para ver su cantidad de vocales: ")
    if (palabra == 'S' or palabra == 's'):
        salir = True
    else:   
        print("La cantidad de vocales que tiene su palabra es: ", cantvocales(palabra), "\n")

    

