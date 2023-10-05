
distancias = []

def lecturadatos():
    try:
        archivo = open("distancias.txt", "r")
        
        for destino in archivo:
            distancias.append(destino.strip()) #Saca el /n de la lista
        archivo.close()
    except:
        print("No se pudo abrir el archivo :/")
    return distancias

def promedio():
    cantidad = len(distancias)
    sumatotal = 0
    for destino in distancias:
        sumatotal += int(destino) #casteo de i
    prom = (sumatotal / cantidad)
    return prom

def maxpromedio():
    for i in range(len(distancias)):
        if (int(distancias[i]) > promedio()):
            print(distancias[i])

print(lecturadatos())
print("El promedio de las distancias es: ", promedio())
maxpromedio()


