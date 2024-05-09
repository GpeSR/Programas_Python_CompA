import os 

class Empleado:
    def __init__(self,nombre,edad,sexo,casado,sueldo): # constructor para inicializar la clase
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
        self.sueldo = sueldo
    def __str__(self): # Generar una salida cuando el objeto es impreso
        return f"\nNombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo =="M" else "Hombre"}, Estado civil: {"Casado(a)" if self.casado else "Soltero(a)"}, Sueldo: {self.sueldo}"

os.system("cls")
empleado01 = Empleado("Jose Diaz", 35, "H", False, 1200) # Instanciacion de un objeto
print("Nombre :", empleado01.nombre)
print("Edad   :", empleado01.edad)
print("sexo   :", empleado01.sexo)
print("Casado :", empleado01.casado)
print(empleado01)

empleado02 = Empleado("Maria Lopez", 40, "M", True, 1400)
print(empleado02)

empleado03 = Empleado("Rocio Soto", 45, "M", False, 2000)
print(empleado03)

total = empleado01.sueldo + empleado02.sueldo + empleado03.sueldo

print("\nTotal del Sueldo: ", total)