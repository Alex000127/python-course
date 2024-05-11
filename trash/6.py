def identificar_dia(numero):
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    if numero >= 1 and numero <= 7:
        dia = dias_semana[numero - 1]
        print(f"El número {numero} corresponde al día {dia}.")


numero = int(input("Ingrese un número del 1 al 7: "))
identificar_dia(numero)