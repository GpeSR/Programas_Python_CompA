# Dividir un numero entero de 4 cifras en sus digitos individuales

import os; os.system("cls")

print("Dividiendo en unidades, decenas, centenas, y millares un numero entero\n")

num = int(input("Ingrese un numero entero de 4 cifras: "))


unidades = num % 10 
num //= 10 
decenas = num % 10
num //= 10
centenas = num % 10
num //= 10
millares = num 


print(f'Millares: {millares}, Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades}')
