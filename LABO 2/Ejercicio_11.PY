cadena = input("Introduce una cadena: ")
es_palindromo = cadena == cadena[::-1]
print(f"¿Es un palíndromo? {es_palindromo}")