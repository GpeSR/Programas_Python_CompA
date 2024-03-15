# Imprime las tablas de multiplicar de la tabla 1 a la n hasta m 

import os; os.system("cls")

print("Imprimiendo las tablas de la 1 a la n hasta m \n")
n = int(input("Hasta que tabla deseas ? "))
m = int(input("Hasta donde la deseas ? "))

for i in range(1,n+1):
	print(f"\nTabla del {i}")
	for j in range(1,m+1):
		print(f"{i} x {j} = {i * j}")
