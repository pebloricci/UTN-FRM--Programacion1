# Ejercicio 3.

with open("productos.txt", "r") as productos:
    for linea in productos:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        
with open("productos.txt", "a") as productos:
    productos.write(input("Ingrese un nuevo producto, precio y cantidad separados por comas: ") + "\n")
print("Producto agregado con éxito.")

#Otra forma de hacerlo sería la siguiente:
# nombre = input("Ingrese el nombre del producto: ")
# precio = input("Ingrese el precio del producto: ")
# cantidad = input("Ingrese la cantidad del producto: ")
# with open("productos.txt", "a") as productos:
#     productos.write(f"{nombre}, {precio}, {cantidad}\n")