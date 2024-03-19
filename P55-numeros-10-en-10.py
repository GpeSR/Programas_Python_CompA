# Imprimir los numeros de 1 a n en intervalos de 10 en 10

import os; os.system("cls")

print("Imprimiendo los numeros de 1 a n en incrementos de 10 en 10 .... \n")
n = int(input("Ingrese hasta que numero desea la sucesion ? "))

for i in range(1, n+1, 10):
    print(i, end=" ")