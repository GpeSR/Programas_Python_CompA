import os

def mayor(c1, c2, c3):
    may = 0
    if c1 > c2 and c1 > c3:
        may = c1
    elif c2 > c1 and c2 > c3:
        may = c2
    elif c3 > c1 and c3 > c2:
        may = c3
    return may

# print(100,30,200)
os.system("cls")
print("Ingrese 3 calificaciones  y se evaluara cual es la mayor de ellas ")
a, b, c = float(input()), float(input()), float(input())
r = mayor(a,b,c)
if r == 0:
    print("\nLas calificaciones son iguales")
else:
    print(f"\nLa calificacion mayor es { r }")