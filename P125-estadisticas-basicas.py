# Funciones para calcular estadisticas

import os, math

def mayor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m:
            m = lista[n]
    return m

def menor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] < m:
            m = lista[n]
    return m

def media(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def varianza(lista, promedio):
    s = 0
    for n in lista:
        s = s + ((n - promedio) ** 2)

    var = (s / len(lista))
    return var

def desv_estandar(var):
    desvE = math.sqrt(var)
    return desvE

# Programa principal
os.system("cls")

numeros = []

while True:
    num = int(input("Ingrese un numero entero ( 0 para terminar ) ? "))
    if num != 0:
        numeros.append(num)
    else:
        break

promedio = media(numeros)
may = mayor(numeros)
men = menor(numeros)
var = varianza(numeros, promedio)
desv = desv_estandar(var)


print(f"\n\nLista de numeros     : {numeros}")
print(f"\nLa media de los datos: {promedio}")
print(f"El mayor de los datos: {may} ")
print(f"El menor de los datos: {men} ")
print(f"Varianza             : {var:.3f} ")
print(f"desviacion estandar  : {desv:.3f} \n")
