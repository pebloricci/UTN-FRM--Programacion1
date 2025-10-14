diccionario = {}

for i in range(5):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    diccionario[clave] = valor
    
clave = input("Ingrese la clave a buscar: ")
if clave in diccionario:        
    print(f"El valor asociado a la clave '{clave}' es: {diccionario[clave]}.")