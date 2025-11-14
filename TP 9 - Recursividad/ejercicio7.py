def contar_bloques(n):
    # Caso base: si el nivel tiene 1 bloque, solo se necesita 1
    if n == 1:
        return 1
    
    # Recursión: bloques del nivel actual + bloques de los niveles superiores
    return n + contar_bloques(n - 1)

num = int(input("Ingrese el número de niveles de la pirámide: "))
print(f"El número total de bloques necesarios para una pirámide de {num} niveles es: {contar_bloques(num)}.")