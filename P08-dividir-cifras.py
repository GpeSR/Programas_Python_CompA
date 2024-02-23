# Dividir un numero entero de 3 cifras en sus digitos individuales

import os; os.system("cls")

print("Dividiendo en unidades, decenas, centenas, y millares un numero entero\n")

#num = int(input("Ingrese un numero entero de 4 cifras: "))
num = int(input("Ingresa tu año de nacimiento: "))

unidades = num % 10 
num //= 10 
decenas = num % 10
num //= 10
centenas = num % 10
num //= 10
millares = num 

numSuerte = millares + centenas + decenas + unidades

print(f'Millares: {millares}, Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades}')
print(f"\n Tu numero de la suerte es: {numSuerte}")
