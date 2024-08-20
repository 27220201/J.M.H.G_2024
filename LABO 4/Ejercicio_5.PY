frase = input("Introduce una frase: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print("El número total de vocales en la frase es:", contador)