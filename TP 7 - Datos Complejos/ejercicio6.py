alumno:str = str()
notas_list:list = []
nota:float = float()
notas_dict:dict = {}
promedio:float = float()

for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno N°{i+1}: ")
    notas_list = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota N°{j+1} del alumno {alumno}: "))
        notas_list.append(nota)
    notas_dict[alumno] = tuple(notas_list)    
    
for i, j in notas_dict.items():
    promedio = sum(j) / 3
    print(f"El promedio de {i} es {promedio}.")