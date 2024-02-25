# Calcular el tercer angulo de un triangulo conociendo dos de sus lados

import os; os.system("cls")

print("Calculando el tercer angulo de un triangulo conociendo dos de sus lados: \n")
print("Ingrese los dos angulos conocidos separados por un espacio: ")

angulo1, angulo2 = (input().split())
angulo1, angulo2 = float(angulo1), float(angulo2)

angulo3 = 180 - (angulo1 + angulo2)

salida = (f"\nLos angulos del triangulo son:\n"
       f"Angulo 1: {angulo1}\n"
       f"Angulo 2: {angulo2}\n"
       f"Angulo 3: {angulo3}\n"
       )

print(salida)