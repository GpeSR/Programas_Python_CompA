# Verificar cual de los tres numeros enteros es mayor

import os; os.system("cls")

print("Verificando el mayor de tres numeros enteros .... \n")
print("Ingrese tres numeros enteros separados por un espacio ? ")

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 == n2 == n3:
    print("\nLos numeros son iguales")
elif n1 >= n2 and n1 >= n3:
    print(f"\nEl mayor es {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"\nEl mayor es {n2}")
elif n3 >= n2 and n3 >= n1:
    print(f"\nEl mayor es {n3}")
    
print("\nProceso Terminado :)")

