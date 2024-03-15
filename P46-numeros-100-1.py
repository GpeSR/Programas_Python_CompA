# Imprimir numeros de 100 a 1 usando for

import os; os.system("cls")

x = int(input("Ingrese el valor inicial para imprimir ? "))
y = int(input("Ingrese el decremento ? "))

print(f"Imprimiendo numeros de {x} a 1 de {y} en {y}...\n")

for c in range(x, 0, -y):
    print(c, end=" ")
