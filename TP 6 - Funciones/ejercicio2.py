def saludar_usuario(nombre):
    nombre = nombre.strip().capitalize()
    print(f"Hola {nombre}!")

nombre:str = input("Ingrese su nombre: ")
saludar_usuario(nombre)     