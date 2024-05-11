colores = ["rojo", "verde", "azul"]

nuevo_color = input("Ingresa un nuevo color: ")
posicion = int(input("Ingresa la posición en la que deseas insertarlo: "))

colores.insert(posicion, nuevo_color)

print("Lista actualizada:", colores)