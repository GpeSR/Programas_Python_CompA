# Imprimir el nombre del mes y los dias del mismo segun el numero que ingrese el usuario 

import os; os.system("cls")

mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

print("Dado un numero introducido por el usuario, imprimir el mes al que corresponde y los dias del mismo ...\n")

while True:
    n = int(input("Ingrese un numero: "))
    if n > 0 and n <= 12:
        break

print(f"\nEl numero {n} corresponde al mes de {mes[n-1]} y tiene {dias[n-1]} dias\n")