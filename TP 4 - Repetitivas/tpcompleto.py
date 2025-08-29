#Ejercicio 1.
for i in range(101):
  print(i)
  
#Ejercicio 2.
numero:int = int(input("Ingrese un numero entero: "))
digitos:str = len(str(numero))

print(f"El numero tiene {digitos} digitos.")  

#Ejercicio 3.
num1:int = int(input("Ingrese el primer numero: "))
num2:int = int(input("Ingrese el segundo numero: "))

for num1 in range(num1+1, num2):
  print(num1)
  
#Ejercicio 4.
eleccion:int = int(1)
suma:int = int(0)

while eleccion != 0:
  eleccion:int = int(input("Ingrese un numero entero a sumar (o 0 para ver el total): "))
  suma+=eleccion
  if eleccion == 0:
    print(f"El total de los numeros enteros sumados es: {suma}.")

#Ejercicio 5.
import random
num_adivinanza:int = int(random.randint(0, 9))
intentos_fallidos:int = int(0)
intento:int = int(0)

while intento != num_adivinanza:
  intento:int = int(input("Adivine un numero entero entre 0 y 9: "))
  if intento != num_adivinanza:
    intentos_fallidos+= 1
    print(f"Numero incorrecto.")
  elif intento == num_adivinanza:
    print(f"Numero correcto. Intentos fallidos: {intentos_fallidos}.") 
    
#Ejercicio 6.
for i in range(100, -1, -1):
  print(i)
  
#Ejercicio 7.
num:int = int(input("Ingrese un numero entero positivo para sumar desde 0 hasta dicho numero: "))
suma:int = int(0)
if num <= 0:
  print("El numero ingresado no es valido.")
elif num > 0:
  for num in range(0, num, 1):
    suma+=num
    print(f"El total de la suma es: {suma}.")
 
#Ejercicio 8.
num:int = int(0)
positivos:int = int(0)
negativos:int = int(0)
pares:int = int(0)
impares:int = int(0)

for i in range(0, 100, 1):
  num = int(input("Ingrese un numero entero: "))
  if num > 0:
    positivos+=1
  elif num < 0:
    negativos+=1
  if num % 2 == 0:
    pares+=1
  elif num % 2 != 0:
    impares+=1

print(f"""
Numeros positivos: {positivos}.
Numeros negativos: {negativos}.
Numeros pares: {pares}.
Numeros impares: {impares}.
      """)

#Ejercicio 9.
num:int = int(0)
prom:float = float(0)
for i in range(0, 100, 1):
  num:int = int(input(f"Ingrese la nota N°{i+1}: "))
  prom+=num

print(f"El promedio de todas las notas es: {prom/100}.")      

#Ejercicio 10.
#Nota: Profe, admito que este ejercicio lo aprendí con IA, no conocía el slicing.
numero = input("Ingresa un numero: ")
numero_invertido = numero[::-1]
print("Numero invertido:", numero_invertido)         