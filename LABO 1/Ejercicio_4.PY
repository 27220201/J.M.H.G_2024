def fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie[:n]
n = int(input("Introduce el número de términos de la serie de Fibonacci: "))
serie_fibonacci = fibonacci(n)
print(f"Los primeros {n} términos de la serie de Fibonacci son: {serie_fibonacci}")
