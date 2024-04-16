# Agregar elementos a un diccionario 

import os; os.system("cls")

print("Agregar elementos a un diccionario de ventas ... \n")
ventas = {"Juan":1550,"Jose":2600,"Maria":2220}
print(f"Diccionario original: {ventas}. Numero de elementos: {len(ventas)}")

print("\nAgregando elementos utilizando ([]) : ") 
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567
print(f"Diccionario de ventas actualizado: {ventas}. Numero de elementos: {len(ventas)}")

print("\nAgregando elementos utilizando (update()) : ") 
ventas.update({"Andrea":9567})
ventas.update({"Miguel":1234})
print(f"Diccionario de ventas actualizado: {ventas}. Numero de elementos: {len(ventas)}\n")
