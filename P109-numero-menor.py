import os 

def num_menor(n1, n2, n3):
    menor  = 0
    if n1 == n2 == n3:
        menor = menor
    elif n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else : 
        menor = n3
    return menor 

os.system("cls")
print("Ingrese tres numeros enteros separados por <Enter> ? ")
n1, n2, n3 = int(input()), int(input()), int(input())
res = num_menor(n1, n2, n3)

if res == 0:
    print("\nLos numeros son iguales ")
else:
    print(f"\nEl numero menor es: {res}")