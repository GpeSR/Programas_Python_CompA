# Conversion de temperaturas de Centigrados a Fahrenheit o viceversa

import os; os.system("cls")

print("Conversion de temperaturas de Centigrados a Fahrenheit o viceversa ... \n")
opcion = str.upper(input("Convertir a [C]entigrados o convertir a [F]ahrenheit ? "))

if opcion == 'C':
    print("\nConvirtiendo a Centigrados...")
    temp = float(input("Ingrese los Grados Fahrenheit ? "))
    res = (temp - 32) * 5 / 9
    print(f"\n{temp} grados Fahrenheit, equivalen a {res:.2f} grados Centigrados")
else :
    print("\nConvirtiendo a Fahrenheit...")
    temp = float(input("Ingrese los Grados Centigrados ? "))
    res = (temp * 9 / 5) + 32
    print(f"\n{temp} grados Centigrados, equivalen a {res:.2f} grados Fahrenheit")