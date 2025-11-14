def suma_digitos(n):
    if n < 10:
        return n
    
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}.")
