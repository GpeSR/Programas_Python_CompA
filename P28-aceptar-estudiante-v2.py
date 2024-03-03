# Sistema de selección para ingreso a la Universidad Kitty Kat SA
# solo se aceptan mujeres mayores de 21 años con promedio entre 8 y 9.5

import os; os.system("cls")

print("Sistema de seleccion para ingreso a la Universidad Kitty Kat SA \n")
nombre = input("Ingrese su nombre ? ")
sexo = input("Ingrese su sexo (h/m) ? ").lower()

if sexo == "m":
    edad = int(input("Ingrese su edad ? "))
    if edad >= 21:
        print("Ingrese sus calificaciones separadas por un espacio ? ")
        c1, c2, c3 = input().split()
        c1, c2, c3 = float(c1), float(c2), float(c3)
        promedio = (c1 + c2 + c3) / 3
        if promedio >= 8 and promedio <= 9.5:
            print(f"\nFelicidades {nombre} has sido aceptada. \nTu edad {edad} años y tus calificaciones {c1}, {c2} y {c3} con promedio de {promedio:.2f} lo permiten.")
        else :
            print(f"\nLo sentimos {nombre} cumples con la edad requerida, pero tu promedio de {promedio:.2f} no esta dentro del rango de aceptacion.\nSolo se aceptan promedios entre 8 y 9.5.")
    else :
        print(f"\nLo sentimos {nombre}, la Universidad Kitty Kat solo acepta mujeres mayores de 21 años.")

elif sexo == "h":
    print(f"\nLo sentimos {nombre}, la Universidad Kitty Kat solo acepta mujeres.")
else :
    print("\nOpción incorrecta")

print("\nProceso terminado")
