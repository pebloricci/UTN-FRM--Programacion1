def fibonacci(n):
    """Función recursiva que retorna el número de Fibonacci en la posición n."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
