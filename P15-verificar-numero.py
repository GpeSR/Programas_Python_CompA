# Verificar si un numero es entero positivo, negativo o cero

import os; os.system("cls")

print("Verificar si un numero entero es positivo, negativo o cero \n")
numero = int(input("Ingrese un numero: "))

if numero > 0:
    print("\nEl numero es positivo")
if numero < 0:
    print("\nEl numero es negativo")
if numero == 0:
    print("\nEl numero es 0")

print("\nProceso terminado ")