# Verificar si la suma de dos numeros es igual a un tercero

import os; os.system("cls")

print("Verificar si la suma de dos numeros es igual a un tercero \n")
print("Ingrese tres numeros enteros separados por Enter ")

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print("\nSon iguales")
else:
    print("\nSon distintos")

print("\nProceso terminado :) ")
