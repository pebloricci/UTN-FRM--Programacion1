def calcular_area_circulo(radio):
    import math
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    return perimetro

radio:float = float(input("Ingrese el radio del círculo: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))