# Calcular el promedio de cinco calificaciones 

import os; os.system("cls")

print("Calculando el promedio .... \n")
nombre = input("Ingresa tu nombre ? ")
print("Ingresa cinco calificaciones separadas por un espacio ? ")


c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = float(c1), float(c2), float(c3), float(c4), float(c5)

promedio = (c1 + c2 + c3 + c4 + c5) / 5

if promedio > 0 and promedio < 6:
    print(f"\n{nombre} tu promedio es: {promedio}. Quedas reprobad@")
elif promedio >= 6 and promedio < 7:
    print(f"\n{nombre} tu promedio es: {promedio}. Pasas de panzazo")
elif promedio >= 7 and promedio < 8:
    print(f"\n{nombre} tu promedio es: {promedio}. Muy bien, puedes mejorar")
elif promedio >= 8 and promedio < 9:
    print(f"\n{nombre} tu promedio es: {promedio}. Excelente, sigue así")
elif promedio >= 9 and promedio <= 10:
    print(f"\n{nombre} tu promedio es: {promedio}. Perfecto, tu esfuerzo valio la pena")

print("\nProceso Terminado :)")
