# Uso de las funciones trigonometricas con el modulo math
import os; os.system("cls")
import math

print('Calculo de funciones trigonometricas\n')
angulo = float(input('Ingrese un angulo (radianes): '))

seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

grados = math.degrees(angulo)

salida = ("\nResumen de funciones trigonometricas \n"
          f"El seno     : {seno}\n"
          f"El coseno   : {cos}\n"
          f"La tangente : {tan}\n"
          f"\nEl angulo {angulo} en radianes, equivale a {grados} grados\n"
          )

print(salida)