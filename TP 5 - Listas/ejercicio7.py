#Ejercicio 7.
autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista original de autos: {autos}")
autos[1], autos[2] = "corsa", "civic"
print(f"Lista modificada de autos: {autos}")

#Otra forma de hacerlo (en este caso especifico, ya que los indices 1 y 2 son consecutivos) 
#sería con slicing: autos[1:3] = "Corsa", "Civic".