import random
opciones = ["piedra", "papel", "tijera"]

usuario = input("Elige piedra, papel o tijera: ").lower()
computadora = random.choice(opciones)

print(f"Tú elegiste: {usuario}")
print(f"La computadora eligió: {computadora}")

if usuario == computadora:
    print("¡Es un empate!")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")