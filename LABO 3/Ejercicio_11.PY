peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "normal"
elif 25 <= imc < 29.9:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"

print(f"Tu IMC es {imc:.2f} y tu categoría es {categoria}.")