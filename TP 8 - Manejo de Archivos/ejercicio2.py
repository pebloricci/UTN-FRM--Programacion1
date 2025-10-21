# Ejercicio 2.

with open("productos.txt", "r") as productos:
    for linea in productos:
        nombre, precio, cantidad = linea.strip().split(", ")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        