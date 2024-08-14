palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if palabra1 < palabra2:
    print(f"{palabra1} va antes que {palabra2} en orden alfabético.")
else:
    print(f"{palabra2} va antes que {palabra1} en orden alfabético.")