#Ejercicio 1.
edad : int = int(input("Ingrese su edad: "))
if edad >= 18:
  print("Es mayor de edad.")
else:
  print("Es menor de edad.")
  
#Ejercicio 2.
nota : float = float(input("Ingrese su nota: "))
if nota >= 6:
  print("Aprobado.")
else:
  print("Desaprobado.")
  
#Ejercicio 3.
num : int = int(input("Ingrese un numero par: "))
if num % 2 == 0:
  print("Es par.")
else:
  print("Es impar.")
  
#Ejercicio 4.
edad : int = int(input("Ingrese su edad: "))
if edad < 12:
  print("Niño/a.")
elif edad >= 12 and edad < 18:
  print("Adolescente.")
elif edad >= 18 and edad < 30:
  print("Adulto/a joven.")
elif edad >= 30:
  print("Adulto.")    
 
#Ejercicio 5.
contrasena : str = str(input("Ingrese su contraseña: "))
largo_contrasena = len(contrasena)
if largo_contrasena >= 8 and largo_contrasena <= 14:
  print("Contraseña adecuada.")
else:
  print("Porfavor ingrese una contraseña de entre 8 y 14 caracteres.")
   
#Ejercicio 6.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
  print(f"Hay sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
  print(f"Hay sesgo negativo o a la izquierda.")
elif media == mediana and media == moda and mediana == moda:
  print(f"No hay sesgo.")
  
#Ejercicio 7.
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)

#Ejercicio 8.
nombre:str = str(input("Ingrese su nombre, porfavor: "))

nombre_mayus = nombre.upper()
nombre_minus = nombre.lower()
nombre_capitalized = nombre.title()


print(f"""
-------------------------------------------------------
      Seleccione como quiere su nombre escrito.
-------------------------------------------------------

                 (1) Mayusculas.
                 (2) Minisculas.
                 (3) Primera letra mayuscula.
-------------------------------------------------------
       """)
eleccion = int(input(" "))

if eleccion == 1:
  print(nombre_mayus)
elif eleccion == 2:
  print(nombre_minus)
elif eleccion == 3:
  print(nombre_capitalized)

#Ejercicio 9.
sismo :float = float(input("Ingrese la magnitudad del terremoto: "))

if sismo > 0 and sismo < 3:
  print("Muy leve.")
elif sismo >= 3 and sismo < 4:
  print("Ligeramente perceptible.")
elif sismo >= 4 and sismo < 5:
  print("Moderado.")
elif sismo >= 5 and sismo < 6:
  print("Fuerte.")
elif sismo >= 6 and sismo < 7:
  print("Muy fuerte.")
elif sismo >= 7 and sismo <= 10:
  print("Extremo.")
else:
  print("El valor ingresado no es valido.")
  
#Ejercicio 10.
print(f"""
-------------------------------------------------------
              Seleccione su hemisferio.
-------------------------------------------------------

                   (1) Norte.
                   (2) Sur.
-------------------------------------------------------
       """)
hemis:int = int(input(" "))

print(f"""
-------------------------------------------------------
                  Seleccione su mes.
-------------------------------------------------------
    (1) Enero  (2) Febrero  (3) Marzo  (4) Abril 
    (5) Mayo   (6) Junio    (7) Julio  (8) Agosto
    (9) Sept.  (10) Oct.    (11) Nov.  (12) Dic.
-------------------------------------------------------
       """)
mes:int = int(input(" "))

dia:int = int(input("Ingrese el día: "))

estacion:str = ""

if hemis == 1:
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or (mes == 3 and dia <= 20))):
        estacion = "Invierno."
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or (mes == 6 and dia <= 20))):
        estacion = "Primavera."
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or (mes == 9 and dia <= 20))):
        estacion = "Verano."
    elif (mes == 9 and dia >= 21) or (mes <= 12 and (mes < 12 or (mes == 12 and dia <= 20))):
        estacion = "Otoño."
elif hemis == 2:
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or (mes == 3 and dia <= 20))):
        estacion = "Verano."
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or (mes == 6 and dia <= 20))):
        estacion = "Otoño."
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or (mes == 9 and dia <= 20))):
        estacion = "Invierno."
    elif (mes == 9 and dia >= 21) or (mes <= 12 and (mes < 12 or (mes == 12 and dia <= 20))):
        estacion = "Primavera."
else:
    estacion = "Hemisferio incorrecto. Seleccione de nuevo."

print("La estación en la que te encuentras es:", estacion)        