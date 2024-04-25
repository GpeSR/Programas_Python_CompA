import os 

def dia_semana(num):
    if num == 1: return "Lunes"
    elif num == 2: return "Martes"
    elif num == 3: return "Miercoles"
    elif num == 4: return "Jueves"
    elif num == 5: return "Viernes"
    elif num == 6: return "Sabado"
    elif num == 7: return "Domingo"
    else : return " "

os.system("cls")
num = int(input("Ingrese un numero (1 - 7) ? "))
dia = dia_semana(num)

if dia == " ":
    print("\nNumero invalido ... ")
else :
    print(f"\nEl dia correspondiente al numero {num} es {dia}")