n = int(input("Introduce un número entero positivo: "))
suma = 0
i = 2

while i <= n:
    suma += i
    i += 2

print("La suma de todos los números pares desde 2 hasta", n, "es:", suma)