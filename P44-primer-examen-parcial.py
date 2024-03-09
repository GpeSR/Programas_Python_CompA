# Control de inscripción a evento académico Universidad Patito SA. de CV.
# Usuarios -- Alumno $100, trabajador $200, docente $500. 
# Paquetes -- Solo conferencias $600, con eventos sociales $800, con kit de acceso $900

import os; 
suma = 0

while(True):
    os.system("cls")
    print("Universidad Patito SA de CV")
    print("Sistema de Inscripción - Congreso de Sistemas \n")

    print("Tipo de usuario: \t\tTipo de paquete:")
    print("[ 1 ] Alumno     $100\t\t[ 1 ] Solo conferencias    $600")
    print("[ 2 ] Trabajador $200\t\t[ 2 ] Con eventos sociales $800")
    print("[ 3 ] Docente    $500\t\t[ 3 ] Con kit de acceso    $900")

    descuento = 0
    
    u = int(input("\nIngrese el tipo de usuario ? "))

    if u > 0 and u < 4:
        if u == 1 : 
            usuario = "Alumno"; precioUs = 100; porDesc = "(20.0%)"; porcentaje = 0.20  
        elif u == 2 : 
            usuario = "Trabajador"; precioUs = 200; porDesc = "(10.0%)"; porcentaje = 0.10  
        elif u == 3 : 
            usuario = "Docente"; precioUs = 500; porDesc = "(5.0%)"; porcentaje = 0.05
            
        p = int(input("Ingrese el tipo de paquete ? "))

        if p > 0 and p < 4:
            if p == 1: 
                paquete = "Solo conferencias"; precioPaq = 600  
            elif p == 2: 
                paquete = "Con eventos sociales"; precioPaq = 800 
            elif p == 3: 
                paquete = "Con kit de acceso"; precioPaq = 900
                

            cant = int(input("Ingrese la cantidad que desea solicitar ? "))

            subtotal = (precioUs + precioPaq) * cant

            if subtotal >= 5000:
                descuento = subtotal * porcentaje
                total = subtotal - descuento 
            else :
                total = subtotal 

                
        else :
            print("\nLa opción seleccionada no es válida")
        
    else :
        print("\n La opción seleccionada no es válida")

    salida = (f"\n----------------------------------------\n"
            f"           Resumen de la venta\n"
            f"----------------------------------------\n"
            f"   Pedido          : {cant}\n"
            f"   Tipo de usuario : {usuario}\n"
            f"   Tipo de paquete : {paquete}\n"
            f"   Subtotal        : {subtotal}\n"
            f"   Descuento       : {descuento} {porDesc}\n"
            f"   Total           : {total}\n"
            f"----------------------------------------\n")
    
    print(salida)
    
    suma = suma + total

    res = input("\nDeseas continuar (S/N) ? ")
    if res.upper() == "N": break

print(f"\nImporte Total de la Venta: {suma}")
print("\nProceso terminado :)")

