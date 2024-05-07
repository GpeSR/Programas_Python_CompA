# Leer un argelo de numeros enteros, luego calcular el factorial de cada numero individual y agregarl a un nuevo arreglo

import os

def facList(numeros):
    lista_fac = []
    for n in numeros:
        f = 1
        for n in range(1, n+1):
            f = f * n
        lista_fac.append(f)
    return lista_fac

# Programa principal
os.system("cls")

numeros = []

while True:
    num = int(input("Ingrese un numero entero ( 0 para terminar ) ? "))
    if num != 0:
        numeros.append(num)
    else:
        break

fac = facList(numeros)
print(f"\nLista de numeros original: {numeros}")
print(f"Lista de factoriales:        {fac} ")