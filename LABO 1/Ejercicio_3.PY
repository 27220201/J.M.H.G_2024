def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
numero = int(input("Introduce un número: "))
resultado = factorial(numero)
print(f"La factorial de {numero} es {resultado}")