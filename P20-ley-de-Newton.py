# Calcular los valores de la segunda ley de Newton (f = m * a)

import os; os.system("cls")

print("Calculando los valores de la segunda ley de Newton... \n")
print("[ f ] = m * a")
print("[ m ] = f / a")
print("[ a ] = f / m")

op = input("Elige una opcion ?").lower() #combierte las letras a minusculas

if op == "f":
    print("\nCalculando la fuerza....")
    m = float(input("Ingrese la masa ? "))
    a = float(input("Ingrese la aceleracion ? "))
    f = m * a
    print("La fuerza es", f)
elif op == "m":
    print("\nCalculando la masa....")
    f = float(input("Ingrese la fuerza ? "))
    a = float(input("Ingrese la aceleracion ? "))
    m = f / a
    print("La masa es", m)
elif op == "a":
    print("\nCalculando la aceleracion....")
    f = float(input("Ingrese la fuerza ? "))
    m = float(input("Ingrese la masa ? "))
    a = f / m
    print("La aceleracion es", a)
else:
    print("Opcion incorrecta")

print("\nProceso terminado \n")
