# Imprimir los numeros de 1 a 100 usando for 

import os; os.system("cls")

x = int(input("Ingrese hasta que valor desea imprimir ? "))
y = int(input("Ingrese el incremento ? "))

print(f"Imprimiendo numeros de 1 a {x} de {y} en {y} ...\n")

for n in range(1, x+1, y):
    print(n, end=" ")