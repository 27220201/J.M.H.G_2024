import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []

    contrasena.append(random.choice(string.ascii_uppercase))
    contrasena.append(random.choice(string.ascii_lowercase))
    contrasena.append(random.choice(string.digits))
    contrasena.append(random.choice(string.punctuation))

    while len(contrasena) < longitud:
        contrasena.append(random.choice(caracteres))

    random.shuffle(contrasena)
    return ''.join(contrasena)

def main():
    longitud_deseada = 12 
    contrasena_segura = generar_contrasena(longitud_deseada)
    print(f"Contraseña segura generada: {contrasena_segura}")

if __name__ == "__main__":
    main()
