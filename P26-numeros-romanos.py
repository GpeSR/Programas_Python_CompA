# Convertir un numero decimal a numero romano 

import os; os.system("cls")

print("Convirtiendo un numero decimal entre 1 y 10 a numero romano... \n")
num = int(input("Ingrese un numero entero entre 1 y 10 ? "))

if num == 1:
    print(f"\nEl numero {num} en notacion romana es I")
elif num == 2:
    print(f"\nEl numero {num} en notacion romana es II")
elif num == 3:
    print(f"\nEl numero {num} en notacion romana es III")
elif num == 4:
    print(f"\nEl numero {num} en notacion romana es IV")
elif num == 5:
    print(f"\nEl numero {num} en notacion romana es V")
elif num == 6:
    print(f"\nEl numero {num} en notacion romana es VI")
elif num == 7:
    print(f"\nEl numero {num} en notacion romana es VII")
elif num == 8:
    print(f"\nEl numero {num} en notacion romana es VIII")
elif num == 9:
    print(f"\nEl numero {num} en notacion romana es IX")
elif num == 10:
    print(f"\nEl numero {num} en notacion romana es X")
else :
    print(f"\nEl numero {num} es invalido")