#Ejercicio 4.
eleccion:int = int(1)
suma:int = int(0)

while eleccion != 0:
  eleccion:int = int(input("Ingrese un numero entero a sumar (o 0 para ver el total): "))
  suma+=eleccion
  if eleccion == 0:
    print(f"El total de los numeros enteros sumados es: {suma}.")