# Multiplicar dos listas de numeros introducidos por el usuario 

import os; os.system("cls")

print("Multiplicando dos listas de cinco numeros .... \n")

lista1 = []
lista2 = []
lista3 = []

print("Ingrese los cinco numeros de la lista 1: ")
for i in range(5):
    n = int(input(f"Lista 1[{i}] = "))
    lista1.append(n)

print("\nIngrese los cinco numeros de la lista 2: ")
for i in range(5):
    n = int(input(f"Lista 2[{i}] = "))
    lista2.append(n)

print("\nCalculando la multiplicacion de los elementos de las listas 1 y 2 ... ")

for i in range(5):
    lista3.append(lista1[i] * lista2[i])

print(f"\nLista 1: {lista1}, {len(lista1)}")
print(f"Lista 2: {lista2}, {len(lista2)}")
print(f"Lista 3: {lista3}, {len(lista3)}\n")
