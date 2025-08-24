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