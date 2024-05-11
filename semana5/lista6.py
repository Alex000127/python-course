# Crear la lista con elementos duplicados
elementos = [1, 2, 3, 4, 2, 5, 6, 2, 7]

# Solicitar al usuario el elemento a eliminar
elemento_a_eliminar = int(input("Ingresa el elemento que deseas eliminar: "))

# Eliminar la primera aparición del elemento utilizando el método remove()
elementos.remove(elemento_a_eliminar)

# Imprimir la lista actualizada
print("Lista actualizada:", elementos)