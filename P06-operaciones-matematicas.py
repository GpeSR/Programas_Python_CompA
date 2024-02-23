# Operaciones matematicas entre 2 numeros

import os; os.system("cls")

print("Haciendo operaciones matematicas con dos numeros flotantes: \n")
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

#x = 9
#y = 2

suma = x + y
resta = x - y
mult = x * y
div = x / y
res = x % y
exp = x ** y
dive = x // y

# alt Z alterna entre linea completa y linea dividida para que se pueda visualizar toda la linea de codigo en pantalla sin que se desplace.

print("\nResultado de las operaciones\n")
print(f'suma: {suma}\nresta: {resta}\nmultiplicacion: {mult}\ndivision: {div}\nresiduo: {res}\nexponenciacion: {exp}\ndivision entera:{dive}')
