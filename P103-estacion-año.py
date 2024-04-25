import os

def estacion(n):
    if n == 1: est = "Primavera"
    elif n == 2: est = "Verano"
    elif n == 3: est = "Otoño"
    elif n == 4: est = "Invierno"
    else: est = " "

    return est

n = int(input("Ingrese la estacion del año (1 - 4) ? "))
est = estacion(n)
if est ==  " ":
    print("Numero de estacion erroneo")
else: 
    print(f"La estacion que corresponde al numero {n} es {est}")