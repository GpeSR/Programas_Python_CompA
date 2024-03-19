# Imprimir secuencia de numeros V1

import os; os.system("cls")

print("Imprimiendo secuencia de numeros V1 ... \n")
n = int(input("Ingrese la cantidad de renglones deseados ? "))

for i in range(1, n+1):
	for j in range(1, i+1):
		print(i, end=" ")
	print("\r")
	
print("\nProceso terminado :)")
