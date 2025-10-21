# Ejercicio 5.

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
        
producto_a_buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for producto in productos:
    if producto["Nombre"].lower() == producto_a_buscar.lower():
        print(f"Producto: {producto['Nombre']} | Precio: ${producto['Precio']} | Cantidad: {producto['Cantidad']}")
        encontrado = True
        break
    
if not encontrado:
    print("Producto no encontrado.")