# Suma 2 listas de numeros introducidas por el usuario 

import os; os.system("cls")

lista1 = []
lista2 = []
lista3 = []

print("Sumar dos listas de n numeros \n")
c = int(input("De cuantos numeros son las listas ? "))

print(f"\nDame los {c} elementos de la lista 1: ")
for i in range(c):
	n = int(input(f"Lista 1[{i}] = "))
	lista1.append(n)

print(f"\nLista 1: {lista1}, {len(lista1)}")

print(f"\nDame los {c} elementos de la lista 2: ")
for i in range(c):
	n = int(input(f"Lista 2[{i}] = "))
	lista2.append(n)

print(f"\nLista 2: {lista2}, {len(lista2)}")

print("\nCalculando la suma de las listas")
for i in range(c):
	lista3.append(lista1[i] + lista2[i])

print(f"Lista 3: {lista3}, {len(lista3)}\n")