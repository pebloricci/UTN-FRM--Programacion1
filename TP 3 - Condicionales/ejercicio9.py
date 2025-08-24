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