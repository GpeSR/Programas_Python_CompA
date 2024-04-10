# Procesa los datos de un estudiante en un diccionario 

import os; os.system("cls")

estudiante = {"nombre": "Juan Perez",
              "edad":45,
              "email":"jperez@msn.com",
              "carrera":"Sistemas"}

estudiante2 = {"nombre": "Maria Lopez",
              "edad":22,
              "email":"maria@msn.com",
              "carrera":"Leyes"}

print(f"El estudiante: \n\n{estudiante}, {len(estudiante)}")

print("\nLas llaves:")
for k in estudiante.keys():
    print(k)

print("\nLos valores:")
for v in estudiante.values():
    print(v)

print("\nModificando los elementos del diccionario ... \n")
estudiante.update({"calificacion":9.5})
estudiante["email"] = "juanp@gmail.com"

for k,v in estudiante.items():
    print(f"{k:<12} : {v:>15}")