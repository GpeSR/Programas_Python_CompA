# Eliminar elementos de un diccionario 

import os; os.system("cls")

print("Eliminar elementos del diccionario de habitantes por municipio ... \n")
municipios = {"Apozol":1863, "Calera":1868, "Fresnillo":1554, "Guadalupe":1821, "Jalpa":1824, "Jerez":1824, "Loreto":1931, "Mazapil":1824, "Momax":1857}
print(f"Diccionario original: {municipios}. Numero de elementos: {len(municipios)}")

print("\nEliminando elementos utilizando (del) : ")
del municipios["Apozol"]
print("Diccionario actualizado:",municipios, "Numero de elementos:",len(municipios))

print("\nEliminando elementos utilizando (pop()) : ")
municipios.pop("Fresnillo")
print("Diccionario actualizado:",municipios, "Numero de elementos:",len(municipios))

print("\nEliminando elementos utilizando (popitem()) : ")
municipios.popitem()
print("Diccionario actualizado:",municipios, "Numero de elementos:",len(municipios))

print("\nEliminando elementos utilizando (clear()) : ")
municipios.clear()
print("Diccionario actualizado:",municipios, "Numero de elementos:",len(municipios),"\n")