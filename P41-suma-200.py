# Suma numeros introducidos por el usuario hasta que la suma sea mayor o igual a 200

import os; 

while(True):
    os.system("cls")

    print("Sumando numeros hasta que el resultado sea mayor o igual a 200 ...\n")

    c = 0
    s = 0

    while(True):
        num = int(input("Ingrese un numero ? "))
        s += num
        c += 1
        if s >= 200:
            break

    print(f"\nSe ingresaron {c} numeros") 
    print(f"La suma es: {s}") 

    res = input("\nDesea continuar (S/N) ? ")
    if res.upper() == "N": break

print("\nProceso terminado :) ")