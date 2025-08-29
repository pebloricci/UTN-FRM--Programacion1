#Ejercicio 7.
num:int = int(input("Ingrese un numero entero positivo para sumar desde 0 hasta dicho numero: "))
suma:int = int(0)
if num <= 0:
  print("El numero ingresado no es valido.")
elif num > 0:
  for num in range(0, num, 1):
    suma+=num
    print(f"El total de la suma es: {suma}.")
