# Tabla de conversion de temperaturas: de Centigrados a Fahrenheit 

import os;

while(True):
    os.system("cls")

    print("Tabla de conversion de grados Centigrados a Fahrenheit ... \n")
    ti = float(input("Ingrese la temperatura inicial en °C: "))
    tf = float(input("Ingrese la temperatura final en °C: "))

    c = ti


    print("\n    Temperatura en grados ")
    print("-"*30)
    print("  °Centigrados\t°Fahrenheit")
    print("-"*30)

    while c <= tf:
        temp = (c * 9 / 5) + 32
        print(f"      {c}\t    {temp:.2f}")
        c = c + 1

    print("-"*30)

    res = input("\nDesea continuar (S/N) ? ")
    if res.upper() == "N": break

print("\nProceso terminado :)")