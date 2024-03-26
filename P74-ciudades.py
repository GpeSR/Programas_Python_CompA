# Capturar una lista de n ciudades hasta introducir $

import os; os.system("cls")

ciudades = []
ciudades_cons = []

print("Capturando el nombre de ciudades \n")
print("Introduce el nombre de n ciudades ($ para terminar) : ")

while True:
	ciudad = input("Ciudad : ")
	if ciudad == "$":
		break
	else:
		ciudades.append(ciudad)
		if ciudad.lower().startswith(('a','e','i','o','u')) == False:
			ciudades_cons.append(ciudad)
			

print(f"\nNumero de elementos de la lista: {len(ciudades)}, {ciudades}\n")

print("Ordenando la lista de forma descendente: ")
ciudades.sort(reverse=True)
print(ciudades)

print(f"\nCiudades que empiezan con consonante: {len(ciudades_cons)}, {ciudades_cons}\n")


