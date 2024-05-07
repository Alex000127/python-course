# Solicitar al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

# Solicitar al usuario que ingrese un carácter para contar
caracter = input("Ingresa un carácter: ")

# Contar cuántas veces aparece el carácter en la frase
contador = frase.count(caracter)

# Mostrar el resultado al usuario
print("El carácter '{}' aparece {} veces en la frase.".format(caracter, contador))