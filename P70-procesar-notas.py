# Procesar n notas (entre 0 y 100) introducidas por el usuario 
# Mostrar notas, # notas, suma, promedio, notas menores al promedio, notaMax y notaMin

import os; os.system("cls")

print("Procesando las notas introducidas por el usuario \n")
print("Capturar n notas en el rango de 1 a 100 (Ingrese 0 para terminar) : ") 
# El rango inicia en 1 porque 0 se usa para terminar la captura, no necesariamente puede ser una nota a capturar 

notas = []
nm = [] # Notas menores al promedio
suma = prom = 0
nMax = nMin = 0
n = 1

while n != 0:
    n = float(input("Nota: "))
    if n > 0 and n <= 100:
        notas.append(n)
        suma += n
    else :
        print("x")

prom = suma / len(notas)

for n in notas:
    if n < prom:
        nm.append(n)
    
salida = (
          f"\n  Resumen del procesamiento \n"
          f"\n  No. de notas    : {len(notas)}\n"
          f"  Notas capturadas: {notas}\n"
          f"  Suma            : {suma}\n"
          f"  promedio        : {prom:.2f}\n"
          f"  Notas menores al promedio: {len(nm)}, {nm}\n"
          f"  Nota maxima     : {max(notas)}\n"
          f"  Nota minima     : {min(notas)}\n")

print(salida)
