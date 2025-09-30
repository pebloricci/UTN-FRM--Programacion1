def calcular_promedio(a, b, c):
    prom = (a + b + c)/3
    return prom

num1:float = float(input("Ingrese el primer número: "))
num2:float = float(input("Ingrese el segundo número: "))
num3:float = float(input("Ingrese el tercer número: "))

print(f"El promedio de las notas es: {calcular_promedio(num1, num2, num3)}.")