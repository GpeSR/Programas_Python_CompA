# Calcular la paga de un trabajador considerando las horas extra

import os; os.system("cls")

print("Calculando la paga de horas extra de un trabajador... \n")

nombre = input("Ingrese el nombre del trabajador > ")
horas = int(input("Ingrese las horas trabajadas > "))
paga = int(input("Ingrese la paga por hora > "))

extra = pagaextra = total = 0 # inicializar variables de resultados 

if horas <= 40 :
    total = horas * paga 
else :
    extra = horas - 40
    pagaextra = extra * paga * 2
    total = (40 * paga) + pagaextra 
    

salida = (f"\nNombre del trabajador: {nombre}\n"
          f"Paga por hora      : {paga}\n"
          f"Horas trabajadas   : {horas}\n"
          f"Horas extra        : {extra}\n"
          f"Paga de horas extra: {pagaextra}\n"
          f"Total de pago      : {total}")

print(salida)

print("\nProceso terminado ")
