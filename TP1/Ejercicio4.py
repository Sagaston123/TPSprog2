num1 = int(input("Ingrese numero 1 (int): "))
num2 = int(input("Ingrese numero 2 (int): "))
num3 = int(input("Ingrese numero 3 (int): "))

if (num1 > num2) and (num1 > num3):
    print(num1, " Es el numero mas grande.")
elif (num2 > num1) and (num2 > num3):
    print (num2, " Es el numero mas grande.")
else:
    print (num3, " Es el numero mas grande.")