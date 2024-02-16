# Leer datos y enviar un saludo 

print('Leyendo datos y enviando un saludo: \n')

nombre = input('Ingrese su nombre: ')    # Lee una cadena 
edad = int(input('Ingrese su edad: '))   # Lee una cadena y la convierte a entero
peso = float(input('Ingrese su peso: ')) # Lee una cadena y la convierte a float

#print('\nTu nombre es ' + nombre + ' tu edad es ' + str(edad) + ' tu peso es ' + str(peso))
#print('Tu nombre es',nombre,'tu edad es',edad,'tu peso es',peso)

print(f'\n{nombre} bienvenid@ a Python, tu edad es {edad}, tu peso es {peso}\n') # Interpolación de cadenas

alerta = peso > 65
print(alerta)

print(type(nombre))
print(type(edad))
print(type(peso))
print(type(alerta))