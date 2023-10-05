from functools import reduce
# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='19-04-2002'  
minombre='Gaston Sagasti'
milegajo=21780
midni=44357988
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01 + 01 + 1989) % 3 = 1992 % 3 = 2

def hashFecha(stringfecha):
    suma = 0
    stringfecha = stringfecha.split('-')
    for i in range(len(stringfecha)):
        suma += int(stringfecha[i])
    return suma % 3
#print(hashFecha(mifecha))





# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: 
# Algoritmo: Toma un par de elementos, los compara, si estan desordenados los ordena, sino los deja como estan, luego procede con el siguiente par hasta llegar al final. Ya en este punto, el ultimo elemento estara ordenado, asi que en la proxima iteracion este no se verificara.

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV
nombre = "datos.csv"
archivo = open(nombre, "r", encoding="utf-8")
lista = [linea.strip().split(', ') for linea in archivo]
listaDic = [{'Nombre': linea[0], 'Precio': float(linea[1]), 'Cantidad': int(linea[2])} for linea in lista]
print(listaDic)
# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.

productoCaro = reduce(lambda x, y: x if x['Precio']>y['Precio'] else y, listaDic)
print("El producto mas caro es: ", productoCaro['Nombre'], " con un precio de: ", productoCaro['Precio'])
productoMenorCantidad = reduce(lambda x,y: x if x['Cantidad']<y['Cantidad'] else y, listaDic)
print("El producto con menor cantidad es: ", productoMenorCantidad['Nombre'], " con una cantidad de: ", productoMenorCantidad['Cantidad'])

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)

def ganancia(lista):
    ganancia = 0
    for i in range(len(lista)):
        ganancia += lista[i]['Cantidad'] * lista[i]['Precio']
    return ganancia

print(ganancia(listaDic))

archivo.close()
#No se me ocurre otra forma en la que pueda usar reduce porque no es mi fuerte el manejo de listas de diccionarios jeje
#Pero se me ocurre otra opcion que seria sin usar reduce:
