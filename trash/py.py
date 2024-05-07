# Concatenación de strings
string1 = "Hola"
string2 = "mundo"
concatenado = string1 + " " + string2
print(concatenado)  # Output: "Hola mundo"

# Repetición de strings
palabra = "Hola"
numero = 3
repetido = palabra * numero
print(repetido)  # Output: "HolaHolaHola"

# Manipulación de strings como arreglos
cadena = "Python"
print(cadena[0])  # Output: "P"
print(cadena[1:4])  # Output: "yth"
print(cadena[-1])  # Output: "n"

# Funciones len, upper y lower
cadena = "Hola Mundo"
print(len(cadena))  # Output: 10
print(cadena.upper())  # Output: "HOLA MUNDO"
print(cadena.lower())  # Output: "hola mundo"

cadena = "Hola mundo"
reemplazada = cadena.replace("mundo", "Python")
print(reemplazada)  # Output: Hola Python