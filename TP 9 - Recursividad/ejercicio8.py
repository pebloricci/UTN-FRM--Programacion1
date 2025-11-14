def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0

    coincidencia = 1 if (numero % 10) == digito else 0
    
    return coincidencia + contar_digito(numero // 10, digito)


num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en el número {num}.")