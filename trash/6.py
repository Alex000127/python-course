def identificar_dia(numero):
    """
    This function takes a number between 1 and 7 as input and returns the corresponding day of the week.
    :param numero: int
    :return: None
    """
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    if numero >= 1 and numero <= 7:
        """
        If the input number is between 1 and 7, the function will return the corresponding day of the week.
        """
        dia = dias_semana[numero - 1]
        print(f"El número {numero} corresponde al día {dia}.")
    else:
        """
        If the input number is not between 1 and 7, the function will print an error message.
        """
        print("El número ingresado no es válido.")

numero = int(input("Ingrese un número del 1 al 7: "))
identificar_dia(numero)