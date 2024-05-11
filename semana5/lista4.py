nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]
nombre_buscar = input("Ingresa un nombre: ")

try:
    indice = nombres.index(nombre_buscar)
    print("El nombre", nombre_buscar, "se encuentra en la posición", indice)
except ValueError:
    print("El nombre", nombre_buscar, "no se encuentra en la lista.")