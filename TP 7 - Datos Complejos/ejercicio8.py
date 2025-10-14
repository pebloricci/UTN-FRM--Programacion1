productos:dict = {"manzana": 15, "banana": 30, "naranja": 25, "pera": 40, "uva": 37, "kiwi": 0}
producto:str = str()
stock:int = int()
eleccion:int = int()

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
    eleccion = int(input("Usted seleccionó: "))
    
    if eleccion == 1:
        producto = input("Ingrese el nombre del producto que desea consultar: ").strip().lower()
        if producto in productos:
            print(f"El stock de {producto} es {productos[producto]} unidades.")
        else:
            print(f"El producto {producto} no se encuentra en el inventario.")
    elif eleccion == 2:
        producto = input("Ingrese el nombre del producto al que desea agregar stock: ").strip().lower()
        if producto in productos:
            stock = int(input(f"Ingrese la cantidad de stock que desea agregar a {producto}: "))
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
            stock = int(input(f"Ingrese la cantidad de stock inicial para {producto}: "))
            if stock >= 0:
                productos[producto] = stock
                print(f"El producto {producto} ha sido agregado con un stock inicial de {stock} unidades.")
            else:
                print("La cantidad de stock inicial debe ser un número no negativo.")
        else:
            print(f"El producto {producto} ya existe en el inventario.")
    elif eleccion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")                                