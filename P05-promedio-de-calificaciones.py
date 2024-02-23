# Calciular el promedio de tres calificaciones

import os # Importa la libreria os que contiene funciones realcionadas al sistema

os.system("cls")
print('Calculando el promedio de 3 calificaciones \n')
print('Ingrese las 3 calificaciones separadas por espacios (pueden incluir decimales): ')

c1, c2, c3 = input().split()
c1, c2, c3 = float(c1), float(c2), float(c3)

prom = (c1 + c2 + c3) / 3

print(f'El promedio de {c1}, {c2}, {c3} es {prom:.2f}')