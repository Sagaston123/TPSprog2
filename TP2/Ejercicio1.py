def invertir_cadena(frase):
    cadena_invertida = ""
    for letra in frase:
        cadena_invertida = letra + cadena_invertida #Este codigo invierte las letras
    return cadena_invertida

frase = input("Ingrese una frase: ")
cadena_invertida = invertir_cadena(frase)
if (cadena_invertida.lower() == frase.lower()): #Chequea si es igual
    print("Es una frase/palabra PALINDROME!")
else: print("No es palindrome :(")
