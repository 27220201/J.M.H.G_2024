def encontrar_primos(n):
    primos = []
    for num in range(2, n):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos
n = int(input("Introduce un número: "))
primos = encontrar_primos(n)
print(f"Los números primos menores que {n} son: {primos}")