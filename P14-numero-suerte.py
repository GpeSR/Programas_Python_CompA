# Calcular el numero de la suerte 

import os; os.system("cls")

print("Calculando el numero de la suerte: \n")
nombre = input("Bienvenido :) \nIngresa tu nombre:")
año = int(input("Ingresa tu año de nacimiento: "))


digito4 = año % 10 
año //= 10 
digito3 = año % 10
año //= 10
digito2 = año % 10
año //= 10
digito1 = año

numSuerte = digito1 + digito2 + digito3 + digito4

salida = (f"\n{nombre} los digitos individuales de tu año de nacimiento son: \n"
          f"Digito 1: {digito1}\n"
          f"Digito 2: {digito2}\n"
          f"Digito 3: {digito3}\n"
          f"Digito 4: {digito4}\n"
          f"\nTu numero de la suerte es: {numSuerte}")

print(salida)
