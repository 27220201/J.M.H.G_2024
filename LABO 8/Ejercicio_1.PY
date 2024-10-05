def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperatura = float(input("Ingresa la temperatura: "))
        unidad = input("¿En qué unidad está? (C o F): ").upper()

        if unidad == "C":
            fahrenheit = celsius_a_fahrenheit(temperatura)
            print(f"{temperatura}°C equivale a {fahrenheit:.2f}°F")
        elif unidad == "F":
            celsius = fahrenheit_a_celsius(temperatura)
            print(f"{temperatura}°F equivale a {celsius:.2f}°C")
        else:
            print("Unidad no válida. Debe ser C o F.")
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.")

if __name__ == "__main__":
    main()
