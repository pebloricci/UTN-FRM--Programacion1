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