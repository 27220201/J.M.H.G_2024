precio_original = float(input("Introduce el precio original del producto: "))
categoria = input("Introduce la categoría del descuento (estudiante, jubilado, empleado, otro): ")

if categoria == "estudiante":
    descuento = 0.10
elif categoria == "jubilado":
    descuento = 0.15
elif categoria == "empleado":
    descuento = 0.05
else:
    descuento = 0.00

precio_final = precio_original * (1 - descuento)
print(f"El precio final es: {precio_final}")