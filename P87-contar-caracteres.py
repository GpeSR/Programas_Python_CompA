# Crear un diccionario con la cantidad de apariciones de un caracter a partir de una cadena introducida por el usuario

import os; os.system("cls")

caracteres = {}
print("Diccionario con el numero de apariciones de cada caracter en una cadena introducida por el usuario ...\n")
print("Diccionario de caracteres: ",caracteres,". Numero de elementos: ",len(caracteres))
cadena = input("\nIngrese una cadena de caracteres ? ")

for i in cadena:
    if i in caracteres:
        caracteres[i] += 1
    else:
        caracteres.update({i:1}) 

print("\nDiccionario de caracteres: ",caracteres,". Numero de elementos: ",len(caracteres),"\n")