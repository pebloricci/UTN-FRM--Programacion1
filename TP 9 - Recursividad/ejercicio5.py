def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False 
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ")
print(es_palindromo(texto))
