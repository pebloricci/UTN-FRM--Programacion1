import math

radio = float(input("Por favor, ingrese el radio del círculo: "))

area = math.floor(math.pi * (radio)**2)

perimetro = math.floor(2 * math.pi * radio)

print(f"El área del círculo es de {area} y el perímetro es de {perimetro}.")