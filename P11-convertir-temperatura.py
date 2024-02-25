# Convertir la temperatura de grados Celcius a grados Fahrenheit

import os; os.system("cls")

print("Convirtiendo la temperatura de grados Celcius a grados Fahrenheit: \n")
celcius = float(input("Ingrese la temperatura en grados Celcius: "))

fahrenheit = (celcius * 9 / 5) + 32

print(f"\nUna temperatura de {celcius} grados Celcius equivale a {fahrenheit} grados Fahrenheit")

