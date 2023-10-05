#Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.
lista = ["Gaston", "Hola", "Soy", "German", "Como va todo", "Menem"]
lista_ordenada = sorted(lista, key=lambda x: len(x))
print(lista_ordenada)