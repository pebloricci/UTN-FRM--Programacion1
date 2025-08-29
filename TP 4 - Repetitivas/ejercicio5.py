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