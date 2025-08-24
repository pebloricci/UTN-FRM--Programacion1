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
