aprobados_parcial1 = {1, 2, 3, 6, 9, 12}
aprobados_parcial2 = {1, 3, 4, 6, 11}
aprobaron_alguno = aprobados_parcial1.union(aprobados_parcial2)

for i in range (len(aprobados_parcial1) + len(aprobados_parcial2)):
    if i in aprobados_parcial1 and i in aprobados_parcial2:
        print(f"El alumno {i} aprobó ambos parciales.")
print("---")
for i in range (len(aprobados_parcial1) + len(aprobados_parcial2)):
    if i in aprobados_parcial1 and not(i in aprobados_parcial2) or i in aprobados_parcial2 and not(i in aprobados_parcial1):
        print(f"El alumno {i} aprobó un solo parcial.")
print("---")

for i in range (len(aprobados_parcial1) + len(aprobados_parcial2)):
    if i in aprobaron_alguno:
        print(f"El alumno {i} aprobó al menos un parcial.")