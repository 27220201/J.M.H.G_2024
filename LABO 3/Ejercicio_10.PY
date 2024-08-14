metros = float(input("Introduce la longitud en metros: "))
unidad = input("Introduce la unidad a la que deseas convertir (pies, pulgadas, yardas): ")

if unidad == "pies":
    conversion = metros * 3.28084
elif unidad == "pulgadas":
    conversion = metros * 39.3701
elif unidad == "yardas":
    conversion = metros * 1.09361
else:
    conversion = "Unidad no válida"

print(f"La longitud en {unidad} es: {conversion}")