# Imprimir numeros pares y numeros impares así como su suma hasta un numero n 

import os

while(True):
    os.system("cls")
    print("Imprimiendo numeros pares e impares de 1 a n y su suma \n")
    n = int(input("Ingrese el limite ? "))

    s = 0
    print("\nNumeros pares y su suma\n")
    for i in range(2, n+1, 2):
        print(i, end=" ")
        s = s+ i
    print("... La suma es ", s)

    s = 0
    print("\nNumeros impares y su suma\n")
    for i in range(1, n+1, 2):
        print(i, end=" ")
        s = s + i
    print("... La suma es ", s)
    
    res = input("\nDesea continuar (S/N) ? ").upper()
    if res == "N": break

print("\nProceso terminado :)")