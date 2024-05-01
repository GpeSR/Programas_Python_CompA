import os

def leer():
    nums = []
    while True:
        d = float(input("Numero ? "))
        if d == -1: break
        nums.append(d)
    return nums

def promedio(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def mayprom(lista,prom):
    mp = []
    for n in lista:
        if n > prom:
            mp.append(n)
    return mp

# Programa principal 
os.system("cls")
nums = leer()
prom = promedio(nums)
mp = mayprom(nums,prom)

print(f"\nLista de numeros: {nums}, {len(nums)}")
print(f"\nEl promedio es: {prom:.2f}")
print(f"Mayores al promedio: {mp}, {len(mp)}\n")