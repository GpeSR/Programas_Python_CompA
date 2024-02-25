# Calcular la paga de un trabajador considerando las horas extra

import os; os.system("cls")

print("Calculando la paga de horas extra de un trabajador (se pagan al doble)... \n")

nombre = input("Ingrese el nombre del trabajador > ")
horas = int(input("Ingrese las horas trabajadas > "))
paga = int(input("Ingrese la paga por hora > "))

extra = 0

if horas > 40 :
    extra = horas - 40
    total = (40 * paga) + (extra * (paga + paga))
else :
    total = horas * paga 

salida = (f"\nNombre del trabajador: {nombre}\n"
          f"Paga por hora   : {paga}\n"
          f"Horas trabajadas: {horas}\n"
          f"Horas extra     : {extra}\n"
          f"Total de pago   : {total}")

print(salida)
