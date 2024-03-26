# Generar dos listas de numeros aleatorios y sumar sus elementos si ambos son impares

import os; os.system("cls")
import random

n = 10
lista1 = []
lista2 = []
lista3 = []

print("Generando listas de numeros aleatorios ... \n")

for i in range(n):
    lista1.append(random.randint(1,20))
    lista2.append(random.randint(1,20))

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

print("\nSumando los elementos de las listas (aplica solo cuando ambos numeros son impares) ...")

for i in range(n):
    if lista1[i] % 2 != 0 and lista2[i] % 2 != 0:
        lista3.append(lista1[i] + lista2[i])
    
print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}\n")