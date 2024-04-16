# Procesar diccionario a partir de dos listas de elementos 

import os; os.system("cls")

print("Procesar un diccionario a partir de dos listas de elementos e iterar sobre esos elementos ... \n")

nombres = ["Juan","Pedro","Manuel","Elias","Maria","Felipe","Julia","Roberto"]
sueldos = [4550.22,8456.88,1235.12,9998.00,12345.50,29456.55,12234.00,2000.00]

print(f"Lista de trabajadores : {nombres}")
print(f"Lista de sueldos      : {sueldos}")

sueldoXtrabajador = dict(zip(nombres,sueldos))
print(f"\nSueldos correspondientes a cada trabajador: \n{sueldoXtrabajador}")

print("\nLas llaves del diccionario : ")
for k in sueldoXtrabajador.keys():
    print(k)

print("\nLos valores del diccionario: ")
for v in sueldoXtrabajador.values():
    print(v)

print("\nIterar usando la llave y el valor en base a la llave : ")
for i in sueldoXtrabajador:
    print(f"{i:<7} - {sueldoXtrabajador[i]}")
    

sum = prom = 0
print("\nLista de trabajadores con suma y promedio de los suledos : ")
for k, v in sueldoXtrabajador.items():
    print(f"{k:<7} : {v:5}")
    sum = sum + v

prom = sum / len(sueldoXtrabajador)
print("\nLa suma de los sueldos es: ",sum)
print("La suma de los sueldos es: ",prom,"\n")