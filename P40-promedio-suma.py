# Calcular la suma y el promedio de los numeros introducidos por el usuario, mostrar cuantos numeros se introdujeron 

import os; 

while(True):
    os.system("cls")

    print("Promedio y suma de numeros (escriba 0 cuando desee detener el ingreso de numeros) ...\n")

    cuenta = suma = 0

    while(True):
        num = int(input("Ingrese un numero ? "))
        if num != 0:
            cuenta +=  1
            suma += num
        else :
            break

    prom = suma / cuenta

    print(f"\nSe ingresaron {cuenta} numeros") 
    print(f"La suma es: {suma}") 
    print(f"El promedio es: {prom:.2f}")  

    res = input("\nDesea continuar (S/N) ? ")
    if res.upper() == "N": break

print("\nProceso terminado :) ")
