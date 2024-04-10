# Procesar dos listas en un diccionario 

import os; os.system("cls")

materias = ["Fisica", "Quimica", "Matematicas", "Geografia", "Estadistica"]
calificaciones = [10,9,8,7.5,6]

print(f"materias : {materias}, {len(materias)}")
print(f"calificaciones : {calificaciones}, {len(calificaciones)}")

notas = dict(zip(materias,calificaciones))

print(f"Las notas : {notas}, {len(notas)}")

print("\nActualizando los elementos del diccionario ...")
notas.update({"Ingles":10})
notas["Programacion"] = 7

print(f"Las notas : {notas}, {len(notas)}")

notas.pop("Fisica") # Elimina un elemento particular
notas.popitem()     # Elimina la ultima entrada del diccionario 

print(f"Las notas : {notas}, {len(notas)}")

notas["Quimica"] = 10
notas.update({"Matematicas":10, "Geografia":10})

print(f"Las notas : {notas}, {len(notas)}")

print("\nLista de materias, suma y promedio:")
s = p = 0
for m, c in notas.items():
    print(f"{m:>12}  - {c:3}")
    s = s + c

p = s / len(notas)

print(f"\nLa suma es {s}, y el promedio es {p}")

notas.clear()
print(f"\nLas notas : {notas}, {len(notas)}")

