def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius:float = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{celsius}°C equivale a {celsius_a_fahrenheit(celsius)}°F.")