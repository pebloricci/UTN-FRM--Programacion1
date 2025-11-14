def calc_factorial_recursivo(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n == 0 or n == 1:
        return 1
    return n * calc_factorial_recursivo(n - 1)

try:
    num = int(input("Ingrese un número entero no negativo para calcular factoriales: "))

    print(f"Factoriales desde 1 hasta {num}:")
    for i in range(1, num + 1):
        print(f"{i}! = {calc_factorial_recursivo(i)}")

except ValueError as e:
    print("Error: Ingrese un valor válido.")
