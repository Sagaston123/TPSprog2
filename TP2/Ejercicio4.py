while True:
    try:
        entrada = input("Ingrese un numero (entero): ")
        numero = int(entrada) #Intento convertir a float
        break
    except ValueError:
        print("Entrada no valida, por favor intente de nuevo.")

digitos = []
numero_str = str(numero)
for dig in numero_str:      #Lista de digitos
    digito = int(dig)
    digitos.append(digito)

def DigMax(digitos):    #Digito mayor
    mAx = 0
    for dig in digitos:
        if(dig > mAx):
            mAx = dig
    return (mAx)
DIGITOMAYOR = DigMax(digitos)
POSICIONMAYOR = digitos.index(DIGITOMAYOR)

print("El digito mayor es: ", DIGITOMAYOR, " y su posicion es: ", POSICIONMAYOR)

