estudiantes = [
    {
        "nombre_apellido" : 'Gaston Sagasti',
        "legajo" : "1234",
        "nota_parcial1" : 61,
        "nota_parcial2" : 83,
        "nota_final" : 76
    },
    {
        "nombre_apellido" : 'Pedro Montenegro',
        "legajo" : "3512",
        "nota_parcial1": 98,
        "nota_parcial2" :79,
        "nota_final" : 89
    },
    {
        "nombre_apellido" : 'Gonzalo Girotti',
        "legajo" : "4321",
        "nota_parcial1" : 47,
        "nota_parcial2" : 74,
        "nota_final" : 59
    },
    {
        "nombre_apellido" : 'Mariano Romero',
        "legajo" : "5214",
        "nota_parcial1" : 72,
        "nota_parcial2" : 54,
        "nota_final" : 69
    }
]

def aprobados(lista):
    nueva_lista = [estud["nombre_apellido"] for estud in estudiantes if estud["nota_parcial1"] > 90 or estud["nota_parcial2"] > 90 or estud["nota_final"] > 90]
    return nueva_lista

print(aprobados(estudiantes))