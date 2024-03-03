# Imprime numeros de n a 1, en decrementos de i

import os; os.system("cls")

n = int(input("Ingrese el inicio ? "))
i = int(input("Ingrese el decremento ? "))

c = n

while c >= 1:
    print(c, end=" ") # imprime c en una sola linea separados por un espacio
    c = c - i