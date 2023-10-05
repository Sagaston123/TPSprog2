def Cargar():
    valido = True
    while valido:
        try:
            alumno_dict = dict()
            cantidad = int(input("Ingrese la cantidad de alumnos: "))
            for i in range(cantidad):
                nombre = input("Ingrese el nombre del alumno: ")
                nota = float(input("Ingrese la nota del alumno: "))
                alumno_dict[nombre] = nota  #Creo un diccionario dentro de la lista
            valido = False
        except ValueError:
            print("Input no valido.")
            
    return alumno_dict 

def Aprobo(nota):
        if (nota >= 40):    #Chequeo si la 'nota' de cada alumno es mayor a 40
            return True
        else: return False

def Mostar():
    diccionario = Cargar()
    items = diccionario.items() 
    print ("{:<10} {:<10} {:<10}".format('ALUMNOS','PARCIAL','RESUTADO'))   #Lindo format para mostrar
    for item in items:
        print("{:<10} {:<10} {:<10}".format(item[0],item[1],'Aprobado' if Aprobo(item[1]) else 'Desaprobado') )

Mostar()

