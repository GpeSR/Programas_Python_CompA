# Lista de numeros impares desde 1 hasta n además de calcular su suma y promedio 
# Mostrar numeros divisibles entre 3 y su suma
# Buscar un elemento en la lista original si esta mostrar la posicion donde se encuentra 

import os; 

os.system("cls")

impares = []
numdiv3 = []
print("Lista de numeros impares desde 1 hasta n \n")
n = int(input("Ingrese n ? "))

suma = suma2 = prom = 0
for i in range(n+1):
    if i % 2 != 0:
        impares.append(i)
        suma += i

prom = suma / len(impares)

for i in range(len(impares)):
    if impares[i] % 3 == 0:
        numdiv3.append(impares[i])
        suma2 += impares[i]

#print(f"Lista de impares hasta n: {impares}")
print(f"\nLa lista de numeros impares hasta {n} tiene {len(impares)} elementos")
print(f"La suma de los numeros impares es: {suma} y el promedio es: {prom}")
print(f"Numeros divisibles entre 3: {len(numdiv3)}, {numdiv3} ")
print(f"La suma de los numeros divisibles entre 3 es: {suma2} \n")

op = input("Desea buscar un elemento en la lista original (S/N) ? ")

if op.upper() == "S":
    buscar = int(input("Ingrese el numero que quiere buscar ? "))
    try:
        pos = impares.index(buscar)
        print(f"\nEl elemento '{buscar}' está en la posición {pos}.")
    except ValueError:
        print(f"\nEl elemento '{buscar}' no está en la lista.\n")
else:
    print("\nProceso terminado :) ")

