# Procesar la informacion de los trabajadores de la empresa Muebles Dico 

import os; os.system("cls")

empleados = []
print(" Mueblería ------ << Muebles Dico >> \nSistema de Procesamiento de Empleados \n")

print("Captura de datos de los empleados (ingrese * para terminar) : ")

while True:
    trabajador = {}
    nombre = input("\nNombre ? ")
    if nombre != "*":
        trabajador["Nombre"] = nombre
        trabajador["Edad"] = int(input("Edad ? "))
        trabajador["Sexo"] = (input("Sexo (h/m) ? ")).lower()
        trabajador["Sueldo"] = float(input("Sueldo ? "))
        empleados.append(trabajador)
    else :
        break

print(f"\nLista de datos de todos los empleados: \n{empleados}")

print("\nTabla de datos: \n")
for k in empleados[0].keys():
    print(f"{k:<10}",end="")
print("\r")
print("-"*40)

sumaEdad = sumaSueldo = hombres = mujeres =  0

for empleado in empleados:
    if empleado["Sexo"] == "h":
        hombres += 1
    else :
        mujeres += 1
    sumaEdad += empleado["Edad"]
    sumaSueldo += empleado["Sueldo"]
    for v in empleado.values():
        print(f"{v:<10}",end="")
    print("\r")
print("-"*40)


print("\nResumen de información : ")
salida = (f"Empleados : {len(empleados)}\n"
          f"Mujeres   : {mujeres}\n"
          f"Hombres   : {hombres}\n"
          f"Edad   --> Suma : {sumaEdad:,},   Promedio : {sumaEdad/len(empleados):,}\n"          
          f"Sueldo --> Suma : {sumaSueldo:,},   Promedio : {sumaSueldo/len(empleados):,}\n"          
          )

print(salida)



