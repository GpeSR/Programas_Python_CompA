# Modificar diccionario utilizando "[]" y utilizando "update"

import os; os.system("cls")

print("Modificar diccionario de paises ....\n")

paises = {"Argentina":100, "Brasil":200, "Colombia":300, "Chile":400, "Ecuador":500, "Bolivia":600, "Jamaica":700}
print(f"Los paises: {paises}, {len(paises)}")

print("\nModificando diccionario utilizando ([]) : ")
paises["Brasil"] = 250
paises["Chile"] = 450
print(f"\nPrimera actualizacion de datos: {paises}, {len(paises)}")

print("\nModificando diccionario utilizando (update()) : ")
paises.update({"Bolivia":650})
paises.update({"Jamaica":750})
print(f"\nSegunda actualizacion de datos: {paises}, {len(paises)}\n")
