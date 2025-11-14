def decimal_a_binario(n):
    if n < 2:
        return str(n)
    
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))
print(f"El número {num} en binario es: {decimal_a_binario(num)}")
