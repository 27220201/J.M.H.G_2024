def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador

cadena = input("Introduce una cadena: ")
numero_vocales = contar_vocales(cadena)
print(f"El número de vocales en la cadena es: {numero_vocales}")