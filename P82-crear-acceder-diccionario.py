# Crear diccionario con los dias de la semana y acceder a sus elementos con distintas tecnicas 

import os; os.system("cls")

print("Diccionario con los dias de la semana ... \n")

dias = {1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado", 7:"Domingo"}

print(f"Elementos del diccionario: {dias}. Numero de elementos: {len(dias)}")

print("\nAcceder a los elementos del diccionario utilizando ([]) : ")
print(f"El primer elemento es: {dias[1]}")
print(f"El ultimo elemento es: {dias[7]}")

print("\nAcceder a los elementos del diccionario utilizando (get()) : ")
print(f"El quinto dia de la semana es : {dias.get(5)}")
print(f"El septimo dia de la semana es: {dias.get(7)}")

print("\nMostrar el diccionario completo : \n")
print("  Llaves - Valores ")
print("."*22)
for k,v in dias.items():
    print(f"    {k:<5}  {v:>5}")
print("."*22)