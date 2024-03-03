# Imprime numeros de 1 a 200, en incrementos de m

import os; os.system("cls")

m = int(input("Multiplos ? "))

c = 0

while c <= 200:
    c += 1
    if c % m != 0:
        continue
    print(c, end=" ")