# Solicitar al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

# Solicitar al usuario que ingrese el carácter a reemplazar y el carácter de reemplazo
caracter = input("Ingresa el carácter a reemplazar: ")
reemplazo = input("Ingresa el carácter de reemplazo: ")

# Realizar el reemplazo en la frase y mostrarla
nueva_frase = frase.replace(caracter, reemplazo)
print("Frase modificada:", nueva_frase)