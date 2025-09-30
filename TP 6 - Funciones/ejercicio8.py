def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso:float = float(input("Ingrese su peso en kg: "))
altura:float = float(input("Ingrese su altura en metros: "))

print(f"Su índice de masa corporal (IMC) es: {calcular_imc(peso, altura)}")