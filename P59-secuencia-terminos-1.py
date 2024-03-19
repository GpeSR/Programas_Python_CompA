# Imprimir secuencia de los terminos armonicos que el usuario desee  

import os; os.system("cls")

print("Imprimiendo secuencia de terminos armonicos \n")

n = int(input("Ingrese la cantidad de terminos deseados ? "))

suma = 0

for i in range(1, n+1):
	if i >= 2: print(f"+ 1/{i}! ", end="")
	else: 
		print(f"{i} ", end="")
	f = 1
	for j in range(1,i+1):
		f = f * j
	suma = suma + 1/f
	
print("\n\nLa suma es: ",suma)
