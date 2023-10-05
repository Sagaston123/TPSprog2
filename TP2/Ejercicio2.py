def EsBisiesto(anio):
    if((anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0):
        return True
    else: return False



valido = False
while(not valido):
    dia = int(input("Ingrese dia: "))
    mes = int(input("Ingrese mes: "))
    anio = int(input("Ingrese anio: "))
    if (mes > 12 or mes < 1):
        print("Mes no valido.")
    elif (dia > 31 or dia < 1):
        print("Dia no valido.")
    elif ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia > 30)):
        print("Dia no valido.")
    elif (mes == 2 and dia >= 29 and not EsBisiesto(anio)):    #Error en el caso 30 de feb de 2012
        print("Dia no valido")
    else: 
        print("DIA VALIDO")
        valido = True



