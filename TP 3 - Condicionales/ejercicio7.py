#Ejercicio 7.
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)