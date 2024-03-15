# Imprimir la tabla de multiplicar que el usuario pida hasta donde lo pida 

import os

while(True): 

	os.system("cls")
	print("Tabla de multiplicar con for: \n")
	t = int(input("Que tabla deseas ? "))
	n = int(input("Hasta donde la deseas ? "))

	for i in range(1,n + 1):
		print(f"{t} x {i} = {t * i}")
	
	res = input("\nDeseas repetir (S/N) ").upper()
	if res == "N": break

print("\nProceso terminado :)")