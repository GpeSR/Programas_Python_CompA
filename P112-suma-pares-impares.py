import os 

def sumaPI(ini, fin, op):
    suma = 0
    if op == "I":
        for i in range (ini, fin + 1):
            if i % 2 != 0:
                #print(i, end=" ")
                suma += i
        return suma
    elif op == "P":
        for i in range(ini, fin + 1):
            if i % 2 == 0:
                #print(i, end=" ")
                suma += i
        return suma 

os.system("cls")
print("Menu de seleccion : ")
print("[ I ] Impares ")
print("[ P ] Pares ")
op = input("Seleccione la opcion deceada ? ").upper()

if op == "P":
    ini = int(input("\nIngrese el numero inicial ? "))
    fin = int(input("Ingrese el numero final ? "))
    s = sumaPI(ini, fin, op)
    print(f"\nLa suma de los numeros pares en el rango ({ini} - {fin}) es: {s}")
elif op == "I":
    ini = int(input("\nIngrese el numero inicial ? "))
    fin = int(input("Ingrese el numero final ? "))
    s = sumaPI(ini, fin, op)
    print(f"\nLa suma de los numeros impares en el rango ({ini} - {fin}) es: {s}")
else: 
    print("\nLa opcion seleccionada es incorrecta. ")