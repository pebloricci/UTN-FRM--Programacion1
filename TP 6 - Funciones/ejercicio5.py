def segundos_a_horas_(segundos):
    horas:float = segundos / 3600
    return horas

segundos:float = float(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundo/s equivale/n a : {segundos_a_horas_(segundos)} hora/s.")