# Calcular la hipotenusa de un triangulo rectangulo a partir de las longitudes de sus lados 

import os; os.system("cls")
import math

print('Calculando la hipotenusa de un triangulo rectangulo: \n')
print('Ingrese los lados del triangulo separados por un Enter: ')

lado1, lado2 = float(input()), float(input()) # Leer dos o mas variables en una sola linea

#hipotenusa = math.sqrt(lado1 * lado1 + lado2 * lado2)
hipotenusa = math.sqrt(math.pow(lado1,2) + math.pow(lado2,2))

print(f'\nEl triangulo de lados {lado1} y {lado2} tiene una hipotenusa de {hipotenusa:.2f}')
