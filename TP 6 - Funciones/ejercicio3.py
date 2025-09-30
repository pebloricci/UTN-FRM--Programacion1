def informacion_personal(nombre, apellido, edad, residencia):
    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()
    residencia = residencia.strip().capitalize()
    print(f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre:str = input("Ingrese su nombre: ")
apellido:str = input("Ingrese su apellido: ")
edad:int = int(input("Ingrese su edad: "))    
residencia:str = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)