# Convertir horas a su equivalente en dias, minutos y segundos 

import os; os.system("cls")

print("Convirtiendo horas a su equivalente en dias, minutos y segundos: \n")
horas = int(input("Ingrese la cantidad de horas: "))

dias = horas / 24
minutos = horas * 60
segundos = minutos * 60
#segundos = horas * 60 * 60

print(f"\n{horas} horas equivale a:\n{dias} dias, {minutos} minutos, {segundos} segundos\n")

# 1 dia tiene 24 horas 
# 1 hora tiene 60 minutos 
# 1 minuto tiene 60 segundos 