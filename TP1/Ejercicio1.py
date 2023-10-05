ladoA = float(input("Ingrese el lado A: "))
ladoB = float(input("Ingrese el lado B: "))
ladoC = float(input("Ingrese el lado C: "))

if ((ladoA == ladoB) and ladoB == ladoC):
    print("El triangulo es EQUILATERO.")
elif ((ladoA != ladoB) and ladoB != ladoC):
    print("El triangulo es ESCALENO.")
else:
    print("El triangulo es ISOCELES.")

