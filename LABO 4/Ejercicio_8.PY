n = int(input("Introduce un número entero positivo: "))

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

print(f"El enésimo número de Fibonacci es: {a}")