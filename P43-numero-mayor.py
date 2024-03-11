# Identificar el numero mayor de una serie de numeros introducidos por el usuario 

import os; 

while(True):
    os.system("cls")

    print("Identificando el mayor de una serie de numeros (escriba 0 cuando desee detener el ingreso de numeros) ...\n")

    m = 0
    while(True):
        num = int(input("Ingrese un numero ? "))
        if num != 0:
            if num > m: m = num
        else :
            break

    print(f"\nEl mayor de los numeros ingresados es: {m}")  

    res = input("\nDesea continuar (S/N) ? ")
    if res.upper() == "N": break

print("\nProceso terminado :) ")
