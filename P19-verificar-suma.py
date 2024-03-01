## Verificar si la suma de dos numeros es igual a un tercero
# 4 5 9   4 8 4   8 4 4    1 2 5    5 5 5 

import os; os.system("cls")

print("Verificar si la suma de dos numeros es igual a un tercero... \n")
print("Ingrese tres numeros enteros separados por espacio: ")

n1, n2, n3 = input().split() # lee una cadena de entrada y separa la cadena cuando hay un espacio
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
    print(f"Caso 1: {n1} + {n2} = {n3}")
elif n1 + n3 == n2:
    print(f"Caso 2: {n1} + {n3} = {n2}")
elif n2 + n3 == n1:
    print(f"Caso 3: {n2} + {n3} = {n1}")
elif n1 == n2 == n3:
    print(f"Caso 4: {n1} = {n2} = {n3}")
else:
    print("Caso 5: Son diferentes y no se suman")

print("\nProceso terminado :)")

