#Ejercicio 5.
contrasena : str = str(input("Ingrese su contraseña: "))
largo_contrasena = len(contrasena)
if largo_contrasena >= 8 and largo_contrasena <= 14:
  print("Contraseña adecuada.")
else:
  print("Porfavor ingrese una contraseña de entre 8 y 14 caracteres.")