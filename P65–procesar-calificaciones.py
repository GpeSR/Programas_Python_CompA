# Procesar n calificaciones introducidas por el usuario 

import os; os.system("cls")

print("Procesando calificaciones \n")
print("Capturar n calificaciones en el rango de 1 a 10 (99 para terminar) \n")

nums = []
mp = []
n = suma = prom = 0

while n != 99:
    n = float(input("Numero: "))
    if n >= 0 and n <= 10:
        nums.append(n)
        suma += n
    else:
        print("x")

prom = suma / len(nums)

for n in nums:
    if n >= prom:
        mp.append(n)

print(f"\nNumeros capturados {len(nums)} : {nums}")
print(f"\nEstadisticas")
print(f"La suma es: {suma} y el promedio es: {prom}. Calificaciones mayores al promedio: {len(mp)} y son {mp}\n")