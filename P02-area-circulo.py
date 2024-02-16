# Calcular el area de un circulo

import math # se importa la libreria de constantes y funciones matemáticas
print('Calculando el area de un circulo: \n')
print('Ingrese el radio del circulo: ')

#radio = float(input('Ingrese el radio del circulo: '))
radio = float(input())

#area = 3.1416 * radio * radio
#area = math.pi * math.pow(radio,2)
area = math.pi * radio ** 2

#print('El circulo de radio',radio,'tiene un area de',area)

print(f'El circulo de radio {radio} tiene un area de {area:.2f}')