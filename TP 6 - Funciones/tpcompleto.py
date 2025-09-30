# Ejercicio 1.
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
print()

# Ejercicio 2.
def saludar_usuario(nombre):
    nombre = nombre.strip().capitalize()
    print(f"Hola {nombre}!")

nombre:str = input("Ingrese su nombre: ")
saludar_usuario(nombre)
print()

# Ejercicio 3.
def informacion_personal(nombre, apellido, edad, residencia):
    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()
    residencia = residencia.strip().capitalize()
    print(f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre:str = input("Ingrese su nombre: ")
apellido:str = input("Ingrese su apellido: ")
edad:int = int(input("Ingrese su edad: "))    
residencia:str = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
print()

# Ejercicio 4.
def calcular_area_circulo(radio):
    import math
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    return perimetro

radio:float = float(input("Ingrese el radio del círculo: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))
print()

# Ejercicio 5.
def segundos_a_horas_(segundos):
    horas:float = segundos / 3600
    return horas

segundos:float = float(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundo/s equivale/n a : {segundos_a_horas_(segundos)} hora/s.")
print()

# Ejercicio 6.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}.")
        
tabla_multiplicar(int(input("Ingrese un número para ver su tabla de multiplicar del 1 al 10: ")))
print()

# Ejercicio 7.
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
print()

# Ejercicio 8.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso:float = float(input("Ingrese su peso en kg: "))
altura:float = float(input("Ingrese su altura en metros: "))

print(f"Su índice de masa corporal (IMC) es: {calcular_imc(peso, altura)}")
print()

# Ejercicio 9.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius:float = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{celsius}°C equivale a {celsius_a_fahrenheit(celsius)}°F.")
print()

# Ejercicio 10.
def calcular_promedio(a, b, c):
    prom = (a + b + c)/3
    return prom

num1:float = float(input("Ingrese el primer número: "))
num2:float = float(input("Ingrese el segundo número: "))
num3:float = float(input("Ingrese el tercer número: "))

print(f"El promedio de las notas es: {calcular_promedio(num1, num2, num3)}.")