def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

# Ejemplo de uso
numero = 7
resultado = es_par_o_impar(numero)
print(resultado)