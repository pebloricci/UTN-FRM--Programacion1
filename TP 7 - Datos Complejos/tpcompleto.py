# Ejercicio 1.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)
print(" ")

# Ejercicio 2.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)
print(" ")

# Ejercicio 3.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

lista = list(precios_frutas.keys())
print(lista)
print(" ")

# Ejercicio 4.
diccionario = {}

for i in range(5):
	clave = input("Ingrese la clave: ")
	valor = input("Ingrese el valor: ")
	diccionario[clave] = valor
    
clave = input("Ingrese la clave a buscar: ")
if clave in diccionario:        
	print(f"El valor asociado a la clave '{clave}' es: {diccionario[clave]}.")
print(" ")

# Ejercicio 5.
frase:str = input("Ingrese una frase: ")

palabras_unicas = frase.split()
print(set(palabras_unicas))

recuento_palabras = {}

if len(palabras_unicas) > 0:
	for i in palabras_unicas:
		recuento_palabras[i] = frase.count(i)
    
print(recuento_palabras)
print(" ")

# Ejercicio 6.
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
print(" ")

# Ejercicio 7.
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
print(" ")

# Ejercicio 8.
productos:dict = {"manzana": 15, "banana": 30, "naranja": 25, "pera": 40, "uva": 37, "kiwi": 0}
producto:str = str()
stock:int = int()
eleccion:int = 0

while eleccion != 4:
	print(f"""
	------------------------------------------------------      
					Supermercadito
	------------------------------------------------------                 
					Elija una opción     
        
				(1) Consultar el stock de un producto.
				(2) Agregar stock a un producto.
				(3) Agregar un nuevo producto.
				(4) Salir.   
	------------------------------------------------------      
		""")
	try:
		eleccion = int(input("Usted seleccionó: "))
	except ValueError:
		print("Opción no válida. Debe ingresar un número del 1 al 4.")
		continue
    
	if eleccion == 1:
		producto = input("Ingrese el nombre del producto que desea consultar: ").strip().lower()
		if producto in productos:
			print(f"El stock de {producto} es {productos[producto]} unidades.")
		else:
			print(f"El producto {producto} no se encuentra en el inventario.")
	elif eleccion == 2:
		producto = input("Ingrese el nombre del producto al que desea agregar stock: ").strip().lower()
		if producto in productos:
			try:
				stock = int(input(f"Ingrese la cantidad de stock que desea agregar a {producto}: "))
			except ValueError:
				print("La cantidad debe ser un número entero.")
				continue
			if stock > 0:
				productos[producto] += stock
				print(f"Se han agregado {stock} unidades a {producto}. Nuevo stock: {productos[producto]} unidades.")
			else:
				print("La cantidad de stock a agregar debe ser un número positivo.")
		else:
			print(f"El producto {producto} no se encuentra en el inventario.")
	elif eleccion == 3:
		producto = input("Ingrese el nombre del nuevo producto que desea agregar: ").strip().lower()
		if producto not in productos:
			try:
				stock = int(input(f"Ingrese la cantidad de stock inicial para {producto}: "))
			except ValueError:
				print("La cantidad debe ser un número entero.")
				continue
			if stock >= 0:
				productos[producto] = stock
				print(f"El producto {producto} ha sido agregado con un stock inicial de {stock} unidades.")
			else:
				print("La cantidad de stock inicial no puede ser negativa.")
		else:
			print(f"El producto {producto} ya existe en el inventario.")
	elif eleccion == 4:
		print("Saliendo del programa...")
		break
	else:
		print("Opción no válida. Por favor, elija una opción del 1 al 4.")
print(" ")

# Ejercicio 9.
agenda:dict = {("Lunes", "14:30"): "Arquitectura y Sistemas Operativos", 
			   ("Martes","15:00"): "Matemática",  
			   ("Miercoles", "14:45"): "Programación I",
			   ("Jueves", "14:00"): "Organización Empresarial",
			   ("Viernes", "16:00"): "Programación I (Consulta)"
			   }

print(f"""
------------------------------------------------------      
				 Agenda Facultativa.
------------------------------------------------------          
	  """)
dia:str = str(input("Ingrese el día a consultar: ")).capitalize()
hora:str = str(input("Ingrese la hora a consultar (formato 24hs, ej: 14:30): "))

if (dia, hora) in agenda:
	print(f"La actividad para el {dia} a las {hora} es: {agenda.get((dia, hora))}")
else:
	print(f"No hay ninguna actividad registrada para el {dia} a las {hora}.")
print(" ")

# Ejercicio 10.
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima", "Colombia": "Bogotá"}

invertido = {}
for pais in original:
	capital = original[pais]
	invertido[capital] = pais
    
print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido}")