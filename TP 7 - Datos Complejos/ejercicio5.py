frase:str = input("Ingrese una frase: ")

palabras_unicas = frase.split()
print(set(palabras_unicas))

recuento_palabras = {}

if len(palabras_unicas) > 0:
    for i in palabras_unicas:
        recuento_palabras[i] = frase.count(i)
    
print(recuento_palabras)