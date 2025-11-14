# Ejercicio 1.
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
print(" ")

# Ejercicio 2.
def fibonacci(n):
    """Función recursiva que retorna el número de Fibonacci en la posición n."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
print(" ")
print(" ")

# Ejercicio 3.
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia_recursiva(base, -exponente)
    return base * potencia_recursiva(base, exponente - 1)

try:
    b = float(input("Ingrese la base (n): "))
    m = int(input("Ingrese el exponente (m) entero: "))
except ValueError:
    print("Entrada inválida. Use un número para la base y un entero para el exponente.")
else:
    resultado = potencia_recursiva(b, m)
    print(f"{b} elevado a {m} = {resultado}")
print(" ")

# Ejercicio 4.
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))
print(f"El número {num} en binario es: {decimal_a_binario(num)}")
print(" ")

# Ejercicio 5.
def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False 
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ")
print(es_palindromo(texto))
print(" ")

# Ejercicio 6.
def suma_digitos(n):
    if n < 10:
        return n
    
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}.")
print(" ")

# Ejercicio 7.
def contar_bloques(n):
    # Caso base: si el nivel tiene 1 bloque, solo se necesita 1
    if n == 1:
        return 1
    
    # Recursión: bloques del nivel actual + bloques de los niveles superiores
    return n + contar_bloques(n - 1)

num = int(input("Ingrese el número de niveles de la pirámide: "))
print(f"El número total de bloques necesarios para una pirámide de {num} niveles es: {contar_bloques(num)}.")
print(" ")

# Ejercicio 8.
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0

    coincidencia = 1 if (numero % 10) == digito else 0
    
    return coincidencia + contar_digito(numero // 10, digito)


num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en el número {num}.")