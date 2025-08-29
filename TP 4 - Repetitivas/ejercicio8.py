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