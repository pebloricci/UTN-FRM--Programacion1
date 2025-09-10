#Ejercicio 1.
lista1 = list(range(0, 101, 4))
print(lista1)

#Ejercicio 2.
lista2 = [5, True, "Hola!", 3.5, "Chauuuu"]
print(lista2[3])

#Ejercicio 3.
lista3 = []
lista3.append("Hola")
lista3.append("¿Cómo")
lista3.append("estás?")
print(lista3)

#Ejercicio 4.
animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista original de animales: {animales}")
animales[1] = "loro"
animales[3] = "oso"
print(f"Lista modificada de animales: {animales}")

#Ejercicio 5.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Ejercicio 6.
lista6 = list(range(10, 30, 5))
print(lista6[0:2])

#Ejercicio 7.
autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista original de autos: {autos}")
autos[1], autos[2] = "corsa", "civic"
print(f"Lista modificada de autos: {autos}")

#Ejercicio 8.
lista8 = [5, 10, 15]
lista_vacia = []
for i in lista8:
  lista_vacia.append(i * 2)
print(lista_vacia)

#Ejercicio 9.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)