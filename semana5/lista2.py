numeros = [1, 2, 3, 4, 5, 2, 3, 2, 1, 4, 2, 3, 2]
numero_buscar = int(input("Ingresa un número: "))
contador = numeros.count(numero_buscar)
print(f"El número {numero_buscar} aparece {contador} veces en la lista.")