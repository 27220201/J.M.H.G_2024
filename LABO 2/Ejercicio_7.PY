anios_vividos = int(input("Introduce el número de años que has vivido: "))

segundos_por_anio = 365 * 24 * 60 * 60  # Número de segundos en un año
segundos_vividos = anios_vividos * segundos_por_anio

print(f"Has vivido durante {segundos_vividos} segundos.")
