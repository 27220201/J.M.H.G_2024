def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir entre cero.")

def main():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operacion = input("¿Qué operación deseas realizar? (+, -, *, /): ")

        if operacion == "+":
            resultado = suma(num1, num2)
        elif operacion == "-":
            resultado = resta(num1, num2)
        elif operacion == "*":
            resultado = multiplicacion(num1, num2)
        elif operacion == "/":
            resultado = division(num1, num2)
        else:
            print("Operación no válida. Debe ser +, -, *, o /.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Entrada inválida. Ingresa números válidos.")

if __name__ == "__main__":
    main()
