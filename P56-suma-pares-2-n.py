# Imprimir los numeros pares de 2 a n y su suma

import os; os.system("cls")

print("Imprimiendo los numeros pares de 2 a n y su suma .... \n")
n = int(input("Ingrese hasta que numero desea la sucesion ? "))

suma = 0

for i in range(2, n+1, 2):
    print(i, end=" ")
    suma += i 

print("\n\nLa suma es:",suma)