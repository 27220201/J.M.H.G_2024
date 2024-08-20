num = int(input("Introduce un número entero positivo: "))

print("Tabla de multiplicar del", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)