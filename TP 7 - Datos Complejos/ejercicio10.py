original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima", "Colombia": "Bogotá"}

invertido = {}
for pais in original:
    capital = original[pais]
    invertido[capital] = pais
    
print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido}")
