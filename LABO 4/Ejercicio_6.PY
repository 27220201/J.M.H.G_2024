num = int(input("Introduce un número entero positivo: "))
suma = 0

while num > 0:
    digito = num % 10
    suma += digito
    num = num // 10

print("La suma de los dígitos es:", suma)