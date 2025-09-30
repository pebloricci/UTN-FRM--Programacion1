def operaciones_basicas(a, b):
    tupla:tuple = (a + b, a - b, a * b, a / b)
    return tupla

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))


if num2 == 0:
    print("Error: No se puede dividir por cero.")
else:
    print(f"""
        Suma: {operaciones_basicas(num1, num2)[0]}
        Resta: {operaciones_basicas(num1, num2)[1]}
        Multiplicación: {operaciones_basicas(num1, num2)[2]}
        División: {operaciones_basicas(num1, num2)[3]}
          """)