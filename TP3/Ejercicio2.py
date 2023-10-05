nombres = ["Gaston", "Gonzalo", "Federico", "Juan", "Mati", "WestVirginia", "Carlos Saul Menem"]

def nooombres(lista, long):
    nueva_lista = [elem for elem in nombres if len(elem)>= long]
    return nueva_lista

print(nooombres(nombres, 9))