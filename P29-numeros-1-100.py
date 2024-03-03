# Imprime numeros de 1 a n, en incrementos de i

import os; os.system("cls")

n = int(input("Ingrese el limite ? "))
i = int(input("Ingrese el incremento ? "))

c = 1

while c <= n:
    print(c, end=" ") # imprime c en una sola linea separados por un espacio
    c = c + i