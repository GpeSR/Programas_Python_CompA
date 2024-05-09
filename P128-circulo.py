import os, math

class Circulo:
    def __init__(self, radio):
        self.radio = radio 
    def obtenerArea(self):
        return math.pi * self.radio ** 2
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Circulo [Radio = {self.radio:.2f}, Area = {self.obtenerArea():.2f}, Circunferencia = {self.obtenerCircunferencia():.2f} ]"
    
# Programa principal 
os.system("cls")
print("Primer Circulo")
circulo01 = Circulo(10.40)
print(f"Radio          : {circulo01.radio:.2f}")
print(f"Area           : {circulo01.obtenerArea():.2f}")
print(f"Circunferencia : {circulo01.obtenerCircunferencia():.2f}")

print(circulo01)

print("\nSegundo Circulo")
circulo02 = Circulo(12.45)
print(circulo02)