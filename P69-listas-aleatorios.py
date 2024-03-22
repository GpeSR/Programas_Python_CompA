# Suma de listas de numeros aleatorios 

import os; os.system("cls")
import random

n = 10
l1 = []
l2 = []
l3 = []

print("Generando listas con numeros aleatorios: \n")
for i in range (n):
	l1.append(random.randint(1,10))
	l2.append(random.randint(1,10))

print(f"Lista 1: {l1}\nlista 2: {l2}")

print("\nElevar los elementos de las listas 1 y 2 al cuadrado \ny sumarlos en la lista 3: ")
for i in range (n):
	l1[i] = l1[i] ** 2
	l2[i] = l2[i] ** 2
	l3.append( l1[i] + l2[i] )

print(f"\nLista 1: {l1}\nlista 2: {l2}\nlista 3: {l3}\n")