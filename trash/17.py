# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Verificar si la palabra es igual a su versión invertida
es_palindromo = palabra == palabra[::-1]

# Mostrar el resultado al usuario
if es_palindromo:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")