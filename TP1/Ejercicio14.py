texto = str(input("Ingrese un texto: "))
texto_toupper = texto.upper()
cant = 0
for i in range(len(texto_toupper) - 1):
    match(texto_toupper[i]):
        case "A", "E", "I", "O", "U":
            cant +=1
        case _:
            continue

print(f"La cantidad de vocales es {cant}")
  


    
    



