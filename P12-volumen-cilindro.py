# Calcular el volumen de un cilindro conociendo su radio y su altura 

import os; os.system("cls")
import math

print('Calculando el volumen de un cilindro: \n')
print('Ingrese el radio y la altura del cilindro separados por un Enter: ')

radio, altura = float(input()), float(input()) # Leer dos o mas variables en una sola linea

volumen = math.pi * (radio * radio) * altura 
#volumen = math.pi * (math.pow(radio,2)) * altura 

print(f'\nEl cilindro de radio {radio} y altura {altura} tiene un volumen de {volumen:.2f}')