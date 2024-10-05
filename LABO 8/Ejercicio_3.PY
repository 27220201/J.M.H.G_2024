import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debes incluir al menos un tipo de caracter.")

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    try:
        longitud = int(input("Longitud de la contraseña: "))
        contrasena_generada = generar_contrasena(longitud)
        print(f"Contraseña generada: {contrasena_generada}")
    except ValueError:
        print("Entrada inválida. Ingresa una longitud válida.")

if __name__ == "__main__":
    main()
