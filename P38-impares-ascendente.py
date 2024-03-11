# Imprimiendo numeros impares de forma ascendente desde 1 hasta n 

import os; 

while(True):
    os.system("cls")

    print("Imprimiendo numeros impares de forma ascendente desde 1 hasta n ... \n")
    n = int(input("Ingrese n ? "))

    c = 1
    s = 0

    while c <= n:
        print(c, end=" ")
        s += c
        c += 2

    print(f"\n\nLa suma de los numeros impares hasta n es: {s}")

    res = input("\nDesea continuar (S/N) ? ")
    if res.upper() == "N": break

print("\nProceso terminado :) ")

