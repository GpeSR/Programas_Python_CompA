import os 

def suma_rango(ini, fin):
    s = 0
    for i in range(ini, fin+1):
        s = s + i
    return s

os.system("cls")
while True:
    i = int(input("Ingrese el inicio ? "))
    f = int(input("Ingrese el fin    ? "))
    if i < f :
        break

print(f"\nLa suma del rango de {i}..{f} = {suma_rango(i,f)}")
