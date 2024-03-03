# Verificar si los numeros son consecutivos
# 9 10 11 son consecutivos; 1 4 6 no son consecutivos

import os; os.system("cls")

print("Verificando si los numeros son consecutivos... \n")
print("Ingrese tres numeros enteros separados por un espacio ? ")

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + 1 == n2 and n2 + 1 == n3: # Verificar si los tres numeros son consecutivos
    print(f"\nLos numeros {n1}, {n2} y {n3} son consecutivos")
elif n1 + 1 == n2 : # verificar si n1 y n2 son consecutivos 
    print(f"\nLos numeros {n1} y {n2} son consecutivos, pero {n3} no lo es")
elif n2 + 1 == n3 : # verificar si n2 y n3 son consecutivos
    print(f"\nLos numeros {n2} y {n3} son consecutivos, pero {n1} no lo es")
else :
    print("\nX ERROR X \nLos numeros no son consecutivos")

print("\nProceso Terminado :)")
    
