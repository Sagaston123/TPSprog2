diccionario = {
    "Gaston" : 21, "Menem" : 45, "Gonza" : 20, "Saul" : 33, "Pedro" : 29, "Mateo" : 15, "Stefano" : 31
}

minimo = int(input("Ingrese la edad minima: "))

pasan = [persona for persona, edad in diccionario.items() if edad > minimo]

print(pasan)