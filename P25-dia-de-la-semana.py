# Verificar el dia de la semana a partir del numero recibido
# 1 es domingo, ..., 7 es sabado

import os; os.system("cls")

print("Mostrar el dia de la semana correspondiente al numero recibido... \n")
num = int(input("Ingrese un numero ? "))

if num == 1:
    print("\nDomingo")
elif num == 2:
    print("\nLunes")
elif num == 3:
    print("\nMartes")
elif num == 4:
    print("\nMiercoles")
elif num == 5:
    print("\nJueves")
elif num == 6:
    print("\nViernes")
elif num == 7:
    print("\nSabado")
else :
    print("\nX ERROR X\nDia Invalido")
