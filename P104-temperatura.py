import os

def fahrenheit(temp):
    return(temp * (9/5) ) + 32

def centigrados(temp):
    return (temp - 32) * (5/9)

# Programa principal
while True:
    os.system("cls")
    print("[ F ] ahrenheit ")
    print("[ C ] entigrados ")
    print("[ S ] alir ")
    op = input("Seleccione una opcion ? ").upper()
    if op == "F":
        temp = float(input("Ingrese la temperatura en °C ? "))
        print(f"\nLos grados fahrenheit son {fahrenheit(temp)}")
    elif op == "C":
        temp = float(input("Ingrese la temperatura en °F ? "))
        print(f"\nLos grados centigrados son {centigrados(temp)}")
    elif op == "S":
        print("Has elegido salir del programa :) ") 
        break
    else:
        print("\nOpcion invalida .... ")

    input("\n<<Presione cualquier tecla para continuar>>")

print("\nGracias por utilizar este programa ")