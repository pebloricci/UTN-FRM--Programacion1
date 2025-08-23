#Ejercicio 1:
print("Hola mundo.")

#Ejercicio 2:
nombre:str=str(input("Ingrese su nombre, porfavor: "))
print(f"Hola {nombre}!")

#Ejercicio 3:
nombre:str=str(input("Ingrese su nombre, porfavor: "))
apellido:str=str(input("Ingrese su apellido, porfavor: "))
edad:str=str(input("Ingrese su edad, porfavor: "))
residencia:str=str(input("Ingrese su residencia, porfavor: "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4:
import math

radio = float(input("Por favor, ingrese el radio del círculo: "))

area = math.floor(math.pi * (radio)**2)

perimetro = math.floor(2 * math.pi * radio)

print(f"El área del círculo es de {area} y el perímetro es de {perimetro}.")

#Ejercicio 5:
segundos:float = float(input("Ingrese la cantidad de segundos: "))

horas = round(segundos / 3600, 2)

print(f"{segundos} segundos equivale a {horas} horas.")

#Ejercicio 6:
num:int = int(input("Ingrese el numero a multiplicar: "))

print(f"""
    {num} x 1 = {num*1}.
    {num} x 2 = {num*2}.
    {num} x 3 = {num*3}.
    {num} x 4 = {num*4}.
    {num} x 5 = {num*5}.
    {num} x 6 = {num*6}.
    {num} x 7 = {num*7}.
    {num} x 8 = {num*8}.
    {num} x 9 = {num*9}.
    {num} x 10 = {num*10}.
       """)

#Ejercicio 7:
num1:int = int(input("Ingrese el primer numero: "))
num2:int = int(input("Ingrese el segundo numero: "))

print(f"""
    {num1} + {num2} = {num1 + num2}.
    {num1} - {num2} = {num1 - num2}.  
    {num1} * {num2} = {num1 * num2}.  
    {num1} / {num2} = {num1 / num2}.  
      """)

#Ejercicio 8:
peso:float = float(input("Ingrese su peso en kilogramos: "))
altura:float = float(input("Ingrese su altura en metros: "))

print(f"Su indice de masa corporal es de {peso/(altura)**2}.")

#Ejercicio 9:
temperatura:float = float(input("Ingrese la temperatura en grados Celsius: "))

print(f"{temperatura}° en Celsius equivale a {(9/5)*temperatura + 32} en Fahrenheit.")

#Ejercicio 10:
num1:float = float(input("Ingrese el primer numero: "))
num2:float = float(input("Ingrese el segundo numero: "))
num3:float = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3)/3

print(f"El promedio de los numeros ingresados es de {promedio}.")