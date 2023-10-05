
def leer_float(mensaje):
    valor = 0
    pedir = True
    while pedir:
        try:
            valor = float(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado no es un numero valido!")


            
    return valor

ancho = leer_float("Ingrese el ancho de la pared: ")
alto = leer_float("Ingrese el alto de la pared: ")
largo = leer_float("Ingrese el largo de la pared: ")
pared_A = ancho * alto
pared_B = largo * alto
puerta = 0.8 * 2
sup_total = (pared_A * 2 + pared_B * 2) - puerta
litros = sup_total / 10

print(f"Para pintar toda la habitacion, que son {sup_total:.2f} metros cuadrados, se necesitan {litros:.2f} de pintura.")
