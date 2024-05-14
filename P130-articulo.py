# Desarrollar una clase llamada Articulo con la informacion de ese articulo

import os
class Articulo:
    def __init__(self, id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
    def obtenerTotal(self):
        return self.precio * self.cantidad
    def __str__(self):
        return f"Informacion del articulo:\nID = {self.id}, Descripcion = {self.descripcion}, Cantidad = {self.cantidad}, Precio = {self.precio}, Total = {self.obtenerTotal()}\n"
    

# Programa principal
os.system("cls")

art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)

art1.cantidad = 999
art1.precio = 0.99
print("\nInformacion del articulo: ")
print("Id          = ",art1.id)
print("Descripcion = ",art1.descripcion)
print("Cantidad    = ",art1.cantidad)
print("Precio      = ",art1.precio)
print("Total       = ",art1.obtenerTotal(),"\n")

art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)

art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)

total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print('Total de todos los articulos:', total)