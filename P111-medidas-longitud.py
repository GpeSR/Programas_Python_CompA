import os 

def centimetros(pul):
    cm = pul * 2.54
    return cm

def pies(mtr):
    ft = mtr * 3.281
    return ft

while True:
    os.system("cls")
    print("Menu de seleccion: \n")
    print("[ cm ] Centimetros ")
    print("[ ft ] Pies ")
    print("[ s  ] Salir ")
    op = input("Elija la opción que desee ? ").lower()

    if op == "cm":
        pul = float(input("\nIngrese la longitud en pulgadas ? "))
        print(f"La longitud en centimetros es {centimetros(pul)}")
    elif op == "ft":
        mtr = float(input("\nIngrese la longitud en metros ? "))
        print(f"La longitud en pies es {pies(mtr)}")
    elif op == "s":
        print("Has elegido salir :( ")
        break
    else: 
        print("Opcion incorrecta ... ")
    
    input("\n<<Presione cualquier tecla para continuar>>")

print("\nGracias por utilizar el programa. ")
