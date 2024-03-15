# Imprimir numeros de 1 a n o de n a 1 segun lo decida el usuario

import os; 

while(True):
    os.system("cls")
    print("\nImprimir los numeros de 1 a n o de n a 1...\n ")
    print("[ 1 ] Numeros de 1 a n ")
    print("[ 2 ] Numeros de n a 1 ")
    print("[ 3 ] Salir ")
    op = int(input("Seleccione una opción ? "))

    if op == 1:
        n = int(input("Ingrese el limite ? "))
        for c in range(1, n+1):
            print(c, end=" ")

    elif op == 2:
        n = int(input("Ingrese el limite ? "))
        for c in range(n, 0, -1):
            print(c, end=" ")

    elif op == 3:
        print("Decidiste salir, adios")
        break
    else: 
        print("\nOpcion incorrecta ")

print("\nProceso terminado, gracias por utilizar este programa ")