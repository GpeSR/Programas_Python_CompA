# Aceptar un estudiante en base a la edad y dos calificaciones

import os; os.system("cls")

print("Universidad Patito SA de CV")
print("Validacion de inscripcion \n")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("\nSolo se aceptan estudiantes mayores de 18 años")
else:
    print("Ingrese dos calificaciones separadas por un <enter>: ")
    c1, c2 = int(input()), int(input())
    if c1 < 8 or c2 < 8:
        print("\nSolo se aceptan estudiantes con calificaciones mayores a 8")
    else: 
        print(f"{nombre}, bienvenido a la Universidad Patito, tu edad {edad} años y tus calificaciones {c1}, {c2} lo permiten")

print("\n Proceso terminado")