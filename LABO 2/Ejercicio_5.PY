try:
    valor_convertido = int('9.8')
except ValueError:
    valor_convertido = None
es_igual = valor_convertido == 10
print(f"El valor de int('9.8') es: {valor_convertido}")
print(f"¿Es igual a 10? {es_igual}")
