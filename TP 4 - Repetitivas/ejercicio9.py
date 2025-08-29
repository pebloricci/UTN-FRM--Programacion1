#Ejercicio 9.
num:int = int(0)
prom:float = float(0)
for i in range(0, 100, 1):
  num:int = int(input(f"Ingrese la nota N°{i+1}: "))
  prom+=num

print(f"El promedio de todas las notas es: {prom/100}.")