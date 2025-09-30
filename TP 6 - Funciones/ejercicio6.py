def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}.")
        
tabla_multiplicar(int(input("Ingrese un número para ver su tabla de multiplicar del 1 al 10: ")))