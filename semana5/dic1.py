# Crear una lista vacía para almacenar las compras
lista_compras = []

# Solicitar al usuario ingresar los elementos de la lista de compras
while True:
    item = input("Ingrese un artículo a la lista de compras (o 'fin' para terminar): ")
    if item.lower() == "fin":
        break
    lista_compras.append(item)

# Mostrar la lista completa de compras al usuario
print("Lista de compras:")
for item in lista_compras:
    print(item)

# Permitir al usuario eliminar elementos de la lista
while True:
    item_eliminar = input("Ingrese el nombre del artículo que desea eliminar (o 'fin' para terminar): ")
    if item_eliminar.lower() == "fin":
        break
    if item_eliminar in lista_compras:
        lista_compras.remove(item_eliminar)
        print(f"El artículo '{item_eliminar}' ha sido eliminado de la lista de compras.")
    else:
        print("El artículo ingresado no se encuentra en la lista de compras.")

# Mostrar la lista actualizada de compras al usuario
print("Lista de compras actualizada:")
for item in lista_compras:
    print(item)