# Calcular el area de un triangulo

print('Calculando el area de un triangulo:\n')
print('Introduzca la base y la altura separados por Enter ')

base, altura = int(input()), int(input()) # Leer dos o mas variables en una sola linea

area = base * altura / 2

print(f'El triangulo de base {base} y altura {altura} tiene un area de {area:.2f}')