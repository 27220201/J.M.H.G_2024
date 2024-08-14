numero = input("Ingresa un número de teléfono de 10 dígitos: ")

if len(numero) == 10 and numero.isdigit():
    formateado = f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"
    print(f"Número formateado: {formateado}")
else:
    print("Por favor, ingresa un número válido de 10 dígitos.")