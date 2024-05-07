# Leer un argelo de numeros enteros, luego sumar los digitos de cada numero individual y agregarlos a un nuevo arreglo

import os

def sumadigitosLista(numeros): 
    listaSuma = []
    for n in numeros:
        suma = 0
        while n != 0:
            dig = n % 10
            suma = suma + dig
            n = n // 10
        listaSuma.append(suma)
    return listaSuma


# Programa principal
os.system("cls")
#num = [1234,4321,1515,2020]
numeros = []

while True:
    num = int(input("Ingrese un numero entero ( 0 para terminar ) ? "))
    if num != 0:
        numeros.append(num)
    else:
        break

suma = sumadigitosLista(numeros)
print(f"\nLista de numeros original: {numeros}")
print(f"Lista de la suma de digitos individuales de los numeros: {suma} ")