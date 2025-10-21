# Ejercicio 4.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad
        }
        productos.append(producto)
print(productos)

